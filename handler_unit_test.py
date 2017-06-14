import task_modules.weather as w
import task_modules.restaurant as r
import task_modules.activity as a
import task_modules.greeting as g
import task_modules.speech as s

# ------------ Weather --------------

#wh = w.WeatherHandler()
#print(wh.get_response())

# ------------ Food --------------
fh = r.FoodHandler()
fh.load_data('data/Food.json')
print(fh.get_response())

# ------------ Activity --------------
ah = a.ActivityHandler()
ah.load_data('data/Activity.json')
print(ah.get_response())

# ------------ Greeting --------------
g = g.GreetingHandler()
print(g.get_response())

# ------------ Speech --------------
s = s.SpeechHandler()
s.load_data('data/Speech.json')
print(s.get_response())

# ------------ SOMETHINGELSE --------------
