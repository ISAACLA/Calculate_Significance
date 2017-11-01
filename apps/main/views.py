from django.shortcuts import render, redirect
from scipy.stats import norm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# def tryout(request):
#     return render(request, 'main/try.html')

def process(request):
    if request.method == 'POST':
        vister1 = float(request.POST['vister1'])
        vister2 = float(request.POST['vister2'])
        convert1 = float(request.POST['convert1'])
        convert2 = float(request.POST['convert2'])

        def standard_error(sample_size, converted):
            p = float(converted) / sample_size
            return ( (p * (1-p) ) / sample_size ) ** 0.5

        def significance(vister1, convert1, vister2, convert2):
            p_one = float(convert1) / vister1
            p_two = float(convert2) / vister2
            se_one = standard_error( vister1, convert1 )
            se_two = standard_error( vister2, convert2 )

            numberator = (p_two - p_one)
            denominator = (se_one ** 2 + se_two ** 2) ** 0.5
            return norm.sf(abs(numberator / denominator))

        p = significance (vister1, convert1, vister2, convert2)
        context = {
            'p': p
        }

        # return render(request, 'main/try.html', context)
        return redirect ('/', context)
