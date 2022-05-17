from django.shortcuts import render


posts = [
	{
		'title' : 'Project Side 1',
		'author' : 'Aniket',
		'date_posted' : 'March 21, 2022',
		'content' : 'All about the project work on side'
	},
	{
		'title' : 'Project Side 2',
		'author' : '**********',
		'date_posted' : 'March 21, 2021',
		'content' : 'All about the project work on side'
	},
	{
		'title' : 'Project Side 3',
		'author' : 'Partner of Aniket',
		'date_posted' : 'June 2, 2019',
		'content' : 'All about the Previous project work on side'
	}

]

business = [
	{
		'1' : 'Construction',
		'2' : 'Hydrocarbon',
		'3' : 'Power',
		'4' : 'Metallurgical & Material Handling',
		'5' : 'Defence',
		'6' : 'Heavy Engineering'
	}
]

industry = [
	{
		'1' : 'Defence Shipbuilding',
		'2' : 'L&T Valves',
		'3' : 'LTI',
		'4' : 'Construction & Mining Machinery',
		'5' : 'L&T Technology Services',
		'6' : 'L&T IDPL'
 	}
]


def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'work/home.html', context)


def about(request):
	context = {
		'info' : 'L&T is a team of more than 50000 \nprofessionals spread across the globe. \nWe combine a proven track record and professional skills, woven together with a culture of trust & caring.'
	}
	return render(request, 'work/about.html', context)

def company(request):
	context = {
		'info' : """Over a decade of sustainability practices and reporting has seen L&T post encouraging results across each of the triple bottom-lines - economic, environmental and social. Our Sustainability Report has been replaced by an Integrated Report which tracks the sustainability performance of the organisation and its interconnectedness with the financial performance, showcasing how L&T is adding value to its stakeholders."""
	}
	return render(request, 'work/company.html', context)

def businesses(request):
	context = {
		'business' : business,
		'industries' : industry
	}
	return render(request, 'work/business.html', context)

def ps(request):
	context = {
		'title' : 'Product & Services'
	}
	return render(request, 'work/ps.html')

def careers(request):
	context = {
		'title' : 'Careers with L&T'
	}
	return render(request, 'work/careers.html', context)
