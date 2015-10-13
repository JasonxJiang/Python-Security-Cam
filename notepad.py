def reverse(text):
	for i in range((len(text)/2)):
		temp = text[i]
		text[i] = text[len(text)-i-1]
		text[len(text)-i-1] = temp
	return text
print reverse("Python")

