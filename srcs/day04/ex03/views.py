from django.shortcuts import render

# Create your views here.

def my_view(request):
	colors = []
	step = 255 // 50
	for i in range(1, 51):
		line = {}
		value = 255 - (i * step)
		line['black'] = f'#{value:02x}{value:02x}{value:02x}'
		line['red'] = f'#{value:02x}0000'
		line['blue'] = f'#0000{value:02x}'
		line['green'] = f'#00{value:02x}00'
		colors.append(line)
	context = {
		'colors' : colors
	}
	return render(request,'ex03/index.html',context)
	