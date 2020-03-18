from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'index.html',{})

def add(request):
	from random import randint

	num_1=randint(0,9)
	num_2=randint(0,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1=request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']
		if  not answer:
			my_ans = "Hey! You Forgot to fill out the answer"
			color="warning"
			return render(request,'divide.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		

		correct_anser=int(old_num_1) + int(old_num_2)
		 
		if int(answer) == correct_anser:
			my_ans="Correct Answer " + old_num_1 + " + " + old_num_2 + " = " + answer
			color = "success" 
			
		else:
		 	my_ans="InCorrect Answer " + old_num_1 + " + " + old_num_2 + " is not " + answer + " it is "+ str(correct_anser)
		 	color =	"danger"
		return render(request,'add.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
	return render(request,'add.html',{
		'num_1':num_1,
		'num_2':num_2,
		})
	

def sub(request):
	from random import randint

	num_1=randint(0,9)
	num_2=randint(0,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1=request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']
		if  not answer:
			my_ans = "Hey! You Forgot to fill out the answer"
			color="warning"
			return render(request,'divide.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
		correct_anser=int(old_num_1) - int(old_num_2)
		 
		if int(answer) == correct_anser:
			my_ans="Correct Answer " + old_num_1 + " - " + old_num_2 + " = " + answer
			color = "success" 
			
		else:
		 	my_ans="Incorrect Answer " + old_num_1 + " - " + old_num_2 + " is not " + answer + " it is "+ str(correct_anser)
		 	color =	"danger"
		return render(request,'sub.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
	return render(request,'sub.html',{
		'num_1':num_1,
		'num_2':num_2,
		})

def divide(request):
	from random import randint

	num_1=randint(0,9)
	num_2=randint(1,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1=request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']
		if  not answer:
			my_ans = "Hey! You Forgot to fill out the answer"
			color="warning"
			return render(request,'divide.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
		correct_anser=int(old_num_1) / int(old_num_2)
		 
		if float(answer) == correct_anser:
			my_ans="Correct Answer " + old_num_1 + " / " + old_num_2 + " = " + answer
			color = "success" 
			
		else:
		 	my_ans="Incorrect Answer " + old_num_1 + " / " + old_num_2 + " is not " + answer + " it is "+ str(correct_anser)
		 	color =	"danger"
		return render(request,'divide.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
	return render(request,'divide.html',{
		'num_1':num_1,
		'num_2':num_2,
		})

def multiply(request):
	from random import randint

	num_1=randint(0,9)
	num_2=randint(0,9)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1=request.POST['old_num_1']
		old_num_2=request.POST['old_num_2']
		if  not answer:
			my_ans = "Hey! You Forgot to fill out the answer"
			color="warning"
			return render(request,'divide.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
		correct_anser=int(old_num_1) * int(old_num_2)
		 
		if int(answer) == correct_anser:
			my_ans="Correct Answer " + old_num_1 + " X " + old_num_2 + " = " + answer
			color = "success" 
			
		else:
		 	my_ans="Incorrect Answer " + old_num_1 + " X " + old_num_2 + " is not " + answer + " it is "+ str(correct_anser)
		 	color =	"danger"
		return render(request,'multiply.html',{
			'answer':answer,
			'my_ans':my_ans,
			'num_1':num_1,
			'num_2':num_2,
			'color':color
			})
		
	return render(request,'multiply.html',{
		'num_1':num_1,
		'num_2':num_2,
		})
