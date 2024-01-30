#Co-Authors - Devin Fan, Sophia Chen
def acc_f1 (tpos, fpos, tneg, fneg):
	
	acc = (tpos + tneg)/(tpos + fpos + tneg + fneg)
	
	percision = tpos / (tpos + fpos)
	
	recall = tpos / (tpos + fneg)
	
	f1 = 2 * ((percision * recall)/(percision + recall))
	
	print("Accuracy is: " , acc + ", F1 Score is:" , f1)
	
	return
	
acc_f1(100, 10, 2, 5)
acc_f1(5, 5, 5, 5)
acc_f1(25, 6, 30, 12)