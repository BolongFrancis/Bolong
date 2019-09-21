import bs4
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from os import path

import wordcloud
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import requests

import matplotlib.pyplot as plt

import re

html = '''
<html>
<head>
<script> var x = 22; var y = 99; print(x,y) </script>
</head>
<body>
<h1 style="text-align: center;">The Best Artificial Intelligence Blogs</h1>
<h2>OpenAI</h2>
<p>The AI researchers at the non-profit AI research company OpenAI are working hard to help us all understand the power of AI as well as the issues that society must work through on this fascinating topic. An important nuance, they seek to enact the path to safe artificial general intelligence.</p>
<p>For more see: <a href="https://openai.com/" target="_blank" rel="nofollow">OpenAI.com</a></p>
<h2>The a16z AI Playbook</h2>
<p>This is not as frequently updated as a blog but it is such a tremendous resource it belongs high on our list. They bring insights on AI topics with a special focus on the creators who are building AI solutions.</p>
<p>For more see: <a href="http://aiplaybook.a16z.com/" target="_blank" rel="nofollow">The a16z AI Playbook</a></p>
<h2>Artificial Intelligence Blog</h2>
<p>They cover AI news, research, books, and thought leaders in the industry. Track for insights into companies and conferences as well.</p>
<p>For more see: <a href="https://www.artificial-intelligence.blog/news/" target="_blank" rel="nofollow">Artificial-Intelligence.blog</a></p>
<h2>Machine Learning Mastery</h2>
<p>Dr. Jason Browlee is a respected practitoner and master of machine learning and he writes for others seeking to really excel at machine learning. Since his focus is on the people who can really execute the blog gets technical, but it is still understandable for the non-technical person who needs to track the big issues.</p>
<p>For more see: <a href="http://machinelearningmastery.com/blog/" rel="nofollow" target="_blank">Machine Learning Mastery</a></p>
<h2>The Algorithmia Blog</h2>
<p>The blog at Algorithmia shares insights, tips and best practices from a team with proven machine learning and data analytics chops.</p>
<p>For more see: <a href="https://blog.algorithmia.com/" rel="nofollow" target="_blank">Algorithmia Blog</a></p>
<h2>AI Trends</h2>
<p>AI trends seeks out and reports on the latest trends in AI for the enterprise, AI research, AI vendors and conferences, including their AI world conference.</p>
<p>For more see: <a href="https://aitrends.com/" rel="nofollow" target="_blank">AITrends</a></p>
<h2>CTOvision</h2>
<p>With a focus on the enterprise CTO, CISO and Chief Data Officer, CTOvision tackles many relevant AI topics including how AI will transform the enterprise.</p>
<p>For more see: <a href="http://ctovision.com" target="_blank">CTOvision</a></p>
<h2>Machine Learnings</h2>
<p>Articles span from the very technical to the very non-technical and their insights are great for all parts of that spectrum.</p>
<p>For more see: <a href="https://machinelearnings.co/" target="_blank" rel="nofollow">MachineLearnings</a></p>
<h2>MIT News AI Site</h2>
<p>MIT News has a special section on AI that captures the latest research and reporting from the academia/education community.</p>
<p>For more see: <a href="http://news.mit.edu/topic/artificial-intelligence2" target="_blank" rel="nofollow">MIT News</a></p>
<h2>Data Robot Blog</h2>
<p>The firm was established by some of the most highly capable data scientists in the world and their blog provides insights on trends and news we should all track.</p>
<p>For more see: <a href="https://www.datarobot.com/blog/" target="_blank" rel="nofollow">DataRobot Blog</a></p>
<h2>Cloudera Vision Blog</h2>
<p>Cloudera provides a platform for all data use cases and workloads including machine learning and artificial intelligence.</p>
<p>For more see: <a href="https://vision.cloudera.com/" target="_blank" rel="nofollow">Cloudera Vision Blog</a></p>
<p>&nbsp;</p>
<p>Did we miss one of your favorite blogs on AI? Have inputs for us on the list? Reach us on Twitter at <a href="http://twitter.com/thingscyber" target="_blank" rel="nofollow">@ThingsCyber</a> or via our <a href="http://thingscyber.wpengine.com/contact-us/" target="_blank" rel="nofollow">Contact Page</a>.</p>
<p>And for more on AI see:</p>

</body>
</html>

'''

html = re.sub(r'<script>.*?</script>','',html)

#html = re.sub(r'For more see.*?</a>','',html)

soup = BeautifulSoup(html,"lxml")
htmlwords = soup.get_text(strip=False)

htmlwords = re.sub(r'\n',' ',htmlwords)

print(htmlwords)

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(htmlwords)

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()