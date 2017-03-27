from django.shortcuts import render
import requests
import parser
import re
import urllib.parse

# Create your views here.


def index(request):
    query_string = urllib.parse.urlencode({"search_query": "emperors new clothes"})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    link = "http://www.youtube.com/embed/" + search_results[0];
    context = {'yt_link':link}
    return render(request, 'index1.html', context)
