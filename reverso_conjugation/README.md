# Reverso Conjugation

This project aims to create JSON files, which store examples of conjugation of verbs.

Sample:

* as a language learner I need examples of Portuguese verb "falar" (means _speak_), something like "I speak" (present tense, 1st person)
* conjugation page starts at http://conjugator.reverso.net/conjugation-portuguese-verb-falar.html
* Python/Selenium performs test while assembling JSON structure with needed examples
* final JSON is saved to file, see output/falar_presente_eu.json

# How to run

In /**reverso_conjugation/** folder, run:

`pytest .`

## Sample console output

```log
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-4.5.0, py-1.8.0, pluggy-0.11.0
rootdir: /home/user/projects/github_open/tutolaq_temp/reverso_conjugation
collected 1 item                                                               

tests_pytest/test_conjugate.py .                                         [100%]

========================== 1 passed in 27.06 seconds ===========================
````
