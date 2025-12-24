from transformers import pipeline
classifier=pipeline("sentiment-analysis")
text="I love my bike"
result=classifier(text)
print("sentiment of text",result)