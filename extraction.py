import boto3
import json

def InitiateClient(service_name='comprehend', region_name ='us-east-2'):
	return boto3.client(service_name = service_name, region_name =region_name)

def DetectEntities(text, threshold = 0.8):
	'''
	Returns a list of titles and creators (person) entities above the threshold
	'''
	comprehend = InitiateClient()
	print('Calling DetectEntities')
	#return json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
	response = comprehend.detect_entities(Text=text, LanguageCode='en')
	entities = response.get("Entities")
	
	titles = []
	creators = []

	for entity in entities:
		if (entity.get("Score", 0) >= threshold) and (entity.get("Type", "") == "TITLE"):
			titles.append(entity.get("Text"))
		elif (entity.get("Score", 0) >= threshold) and (entity.get("Type", "") == "PERSON"):
			creators.append(entity.get("Text"))

	return {
	"Titles" : titles,
	"Creators" : creators
	}


def DetectSyntax(text, threshold = 0.8):
	'''
	Returns a list of adjectives above the threshold level
	'''
	comprehend = InitiateClient()
	print('Calling DetectSyntax')
	#return json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
	response = comprehend.detect_syntax(Text=text, LanguageCode='en')
	tokens = response.get("SyntaxTokens")
	
	adjectives = []
	for token in tokens:
		POS = token.get("PartOfSpeech")
		if (POS.get("Tag") == "ADJ") and (POS.get("Score") >= threshold):
			adjectives.append(token.get("Text"))

	return {
	"Adjectives" : adjectives
	}


def DetectKeyPhrases(text):
	comprehend = InitiateClient()
	print('Calling DetectKeyPhrases')
	print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))


if __name__ == "__main__":
	pass

	#tests below

	#input_str = "House of Spirits by Isabel Allende"

	'''
	input_str = """Life After Life by Kate Atkinson

	The First Fifteen Lives of Harry August by Claire North

	The Psychology of Time Travel by Kate Mascarenhas

	All the Birds in the Sky by Charlie Jane Anders"""
	'''

	'''
	input_str = """Magical realism thats easy to read?
	A perfect example of this would be Blindness by Jose Saramago, but of course I've already read it. I also really enjoyed Love in the Time of Cholera. I like how those books had really simple prose, that subtly blurred the lines of reality, and have a dreamlike quality to them.
	I tried to pick up One Hundred Years of Solitude, but it's just too much for me right now. I need something thats a little simpler, and easy to read."""
	'''
	
	#print(DetectEntities(input_str))

	#print(DetectSyntax(input_str))

	