import pickle
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
f = open("langs.pkl","wb")
pickle.dump(dict,f)
f.close()

with open('langs.pkl','rb') as pb:
    phonebook = pickle.load(pb)

print(phonebook)