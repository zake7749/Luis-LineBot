# Luis-LineBot

This is a demo of how to use and connect Mircosoft Language Understanding Intelligent Service(LUIS) to chatbot server.

<div align="center"><img src="http://i.imgur.com/u6CGvsr.png"></div>

## LuisWrapper

LuisWrapper which is a wrapper of [Cognitive-LUIS-Python](https://github.com/Microsoft/Cognitive-LUIS-Python) provides an interface of intent classification. We can initialize it by a string of LUIS_APPID and LUISAPPKEY that can be found in your app main page on LUIS platforms.

```python
from luis_wrapper import LuisWrapper
luis_wrapper = LuisWrapper(YOUR_LUIS_APPID, YOUR_LUIS_APPKEY)
```

We can sent a requset to LUIS by calling `luis_wrapper.predict(query)`, which return the top intent and some entities found in the query.

```python
query = 'Hello! How are you?'
top_intent, entities = luis_wrapper.predict(query)
```

For more details on connecting a chatbot server to Line, please refer [Line-Chatbot](https://github.com/zake7749/Line-Chatbot)(django) or [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)(flask)
