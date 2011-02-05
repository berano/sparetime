import urllib,urllib2,re,sys,xbmcplugin,xbmcgui
import xbmcaddon,os
import StringIO
pluginhandle = int(sys.argv[1])


nick=xbmcaddon.Addon(id='plugin.video.nickelodeon')
pluginhandle = int(sys.argv[1])


def xbmcpath(path,filename):
     translatedpath = os.path.join(xbmc.translatePath( path ), ''+filename+'')
     return translatedpath

def openfile(filename):
     fh = open(filename, 'r')
     contents=fh.read()
     fh.close()
     return contents

def save(filename,contents):  
     fh = open(filename, 'w')
     fh.write(contents)  
     fh.close()

fptpath = 'special://profile/addon_data/'
translatedfptpath = xbmcpath(fptpath,'')
referer = xbmcpath(fptpath,'ref.txt')

def CATS():
        addDir('nick.com','http://www.nick.com/videos/',1,'','')
        addDir('nickjr.com','http://www.nickjr.com/video/index.jhtml',14,'','')

def CATSJR():
        addDir('Videos','http://www.nickjr.com/common/data/kids/get-kids-config-data.jhtml?fsd=/dynaboss&urlAlias=kids-video-landing',10,'','')
        addDir('Channels','http://www.nickjr.com/video/index.jhtml',11,'','')


def SHOWSJR(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        names = re.compile('"title":"(.+?)"').findall(link)
        thumbs = re.compile('"thumbnail":"(.+?)"').findall(link)
        urls = re.compile('"link":"(.+?)"').findall(link)
	videos = [(names[i],thumbs[i],urls[i])for i in range (0,len(thumbs))]
	for name,thumb,url in videos:
		addDir(name.replace('&amp;','&'),'http://www.nickjr.com'+url,12,'http://www.nickjr.com/'+thumb,'')

def CHANNELS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        all=re.compile('<span>Channels</span>.+?<span>Shows</span>', re.DOTALL).findall(link)
	match=re.compile('<a href=".+?id=(.+?)" id=".+?">(.+?)</a>').findall(all[0])	
	for url,name in match:
		addDir(name.replace('&amp;','&'),'http://www.nickjr.com/dynamo/video/data/mrssGen.jhtml?type=network&loc=sidebar&hub=njParentsHub&mode=playlist&mgid=mgid:cms:item:nickjr.com:'+url,13,'','')

def SUBSHOWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        urlalias = re.compile('"urlAlias", "(.+?)"').findall(link)[0]
        req = urllib2.Request('http://www.nickjr.com/common/data/kids/get-kids-config-data.jhtml?fsd=/dynaboss&urlAlias='+urlalias)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        names = re.compile('"title":"(.+?)"').findall(link)
        thumbs = re.compile('"thumbnail":"(.+?)"').findall(link)
        urls = re.compile('"id":"(.+?)"').findall(link)
	videos = [(names[i],thumbs[i],urls[i])for i in range (0,len(thumbs))]
	for name,thumb,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.nickjr.com/dynamo/video/data/mediaGen.jhtml?mgid=mgid:cms:item:nickjr.com:'+url+'&block=false',name)+"&mode="+str(15)
                item=xbmcgui.ListItem(name.replace('&amp;','&'), thumbnailImage=thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def SUBCHANNELS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        names = re.compile('<media:title>(.+?)</media:title>').findall(link)
        urls = re.compile('<media:player url="http://media.mtvnservices.com/mgid:cms:item:nickjr.com:(.+?)"/>').findall(link)
	videos = [(names[i],urls[i])for i in range (0,len(names))]
	for name,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.nickjr.com/dynamo/video/data/mediaGen.jhtml?mgid=mgid:cms:item:nickjr.com:'+url+'&block=false',name)+"&mode="+str(15)
                item=xbmcgui.ListItem(name.replace('&amp;','&'))
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def SHOWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        all=re.compile('href="/overlay/login.html">Log in</a>.+?<a href="/thebighelp"', re.DOTALL).findall(link)
	match1=re.compile('<a href="/shows/(.+?)" style="background-image.+?http://nick.mtvnimages.com/nick-assets/navigation/shownav/(.+?).jpg.+?".+?title="(.+?)"').findall(all[0])
	addDir('Spongebob Squarepants','http://spongebob.nick.com/',2,'http://nick.mtvnimages.com/nick-assets/navigation/shownav/menu_icon_spongebob.jpg','')
	addDir('NickNews','http://news.nick.com/',2,'http://nick.mtvnimages.com/nick-assets/navigation/shownav/menu_icon_nicknews.jpg','')		
	for url,thumb,name in match1:
		addDir(name.replace('&amp;','&'),'http://www.nick.com/shows/'+url,2,'http://nick.mtvnimages.com/nick-assets/navigation/shownav/'+thumb+'.jpg','')

def CATSPONGE(url):
	if url.find('spongebob')>0:
		save(referer,'dummy')
        	addDir('Full Episodes','http://spongebob.nick.com/ajax/videos/full-episodes/?_&sort=date+desc&start=0&page=1&type=fullEpisodeItem&viewType=fullEpisodesVideosCarousel',4,'','')
        	addDir('Clips','http://spongebob.nick.com/ajax/videos?_&sort=date+desc&start=0&page=1&type=videoItem&updateDropdown=true&viewType=collectionAll&rows=21',3,'','')
	elif url.find('news.nick')>0:
		save(referer,'dummy')
		addDir('Full Episodes','http://www.nick.com/ajax/videos/nick-news-videos?_&sort=date+desc&start=0&page=1&type=fullEpisodeItem',8,'','')
        	addDir('Clips','http://www.nick.com/ajax/videos/nick-news-videos?_&sort=date+desc&start=0&page=1',7,'','')
	else:   
		req = urllib2.Request(url)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	page = urllib2.urlopen(req)
		link = page.read()
		ref = re.compile('class=""><a href="/videos/(.+?)"').findall(link)[0]
		save(referer,ref)
        	addDir('Full Episodes','http://www.nick.com/ajax/videos/'+ref+'?_&sort=date+desc&start=0&page=1&type=fullEpisodeItem',4,'','')
        	addDir('Clips','http://www.nick.com/ajax/videos/'+ref+'?_&sort=date+desc&start=0&page=1&type=videoItem',3,'','')

#http://www.nick.com/ajax/videos/nick-news-videos?_=1296832220417&sort=date+desc&start=0&page=1&type=fullEpisodeItem EPISODE NEWS
#http://www.nick.com/ajax/videos/nick-news-videos?_=1296832008835&sort=date+desc&start=0&page=1 ALL NEWS

def CATALL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
	urlname = re.compile('class=""><a href="/videos/(.+?)"').findall(link)[0]
	for url in urlname:
        	addDir('Full Episodes','http://www.nick.com/ajax/videos/'+url+'?_&sort=date+desc&start=0&page=1&type=fullEpisodeItem',4,'','')
        	addDir('Clips','http://www.nick.com/ajax/videos/'+url+'?_&sort=date+desc&start=0&page=1&type=videoItem',3,'','')

def CLIPSNEWS(url):
       		req = urllib2.Request(url)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req).read()
		code=re.sub('&quot;','',response)
		code1=re.sub('&#039;','',code)
		code2=re.sub('&#215;','',code1)
		code3=re.sub('&#038;','',code2)
		code4=re.sub('&#8216;','',code3)
		code5=re.sub('&#8217;','',code4)
		code6=re.sub('&#8211;','',code5)
		code7=re.sub('&#8220;','',code6)
		code8=re.sub('&#8221;','',code7)
		code9=re.sub('&#8212;','',code8)
    		code10=re.sub('&amp;','&',code9)
        	code11=re.sub("`",'',code10)
		match=re.compile('"cmsid">(.+?)</div><div style="display:none;" class="item-type">video</div><div style="display:none;" class="screenshot">.+?</div><a title="(.+?)" href=".+?".+?<img alt=".+?" border=".+?" height=".+?" width=".+?" src="(.+?)"').findall(code11)
		for url,name,thumb in match:
			addDir(name.replace('&amp;','&'),'http://www.nick.com/dynamo/video/data/mrssGen.jhtml?type=network&hub=home&loc=default&mode=episode&dartSite=nick.nol&mgid=mgid:cms:video:nick.com:'+ url +'&demo=null&block=true',9,thumb,'')
		i=0
		for i in range (i+19):
			pagenumber = str(21*i+21)
			addDir('Page '+str(i+2),'http://www.nick.com/ajax/videos/nick-news-videos?_&sort=date+desc&start='+pagenumber+'&page=1&type=videoItem',7,'','')

def CLIPS(url):
	if url.find('spongebob')>0:
       		req = urllib2.Request(url)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req).read()
		code=re.sub('&quot;','',response)
		code1=re.sub('&#039;','',code)
		code2=re.sub('&#215;','',code1)
		code3=re.sub('&#038;','',code2)
		code4=re.sub('&#8216;','',code3)
		code5=re.sub('&#8217;','',code4)
		code6=re.sub('&#8211;','',code5)
		code7=re.sub('&#8220;','',code6)
		code8=re.sub('&#8221;','',code7)
		code9=re.sub('&#8212;','',code8)
    		code10=re.sub('&amp;','&',code9)
        	code11=re.sub("`",'',code10)
		match=re.compile('"cmsid">(.+?)</div><div style="display:none;" class="item-type">video</div><div style="display:none;" class="screenshot">.+?</div><a title="(.+?)" href=".+?".+?<img alt=".+?" border=".+?" height=".+?" width=".+?" src="(.+?)"').findall(code11)
		for url,name,thumb in match:
			addDir(name.replace('&amp;','&'),'http://www.nick.com/dynamo/video/data/mrssGen.jhtml?type=network&hub=home&loc=default&mode=episode&dartSite=nick.nol&mgid=mgid:cms:episode:spongebob.com:'+ url +'&demo=null&block=true',5,thumb,'')
		i=0
		for i in range (i+19):
			pagenumber = str(21*i+21)
			addDir('Page '+str(i+2),'http://spongebob.nick.com/ajax/videos/all-videos/?_=&sort=date+desc&start='+pagenumber+'&page=0&updateDropdown=true&viewType=collectionAll',3,'','')
	else:
        	req = urllib2.Request(url)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req).read()
		code=re.sub('&quot;','',response)
		code1=re.sub('&#039;','',code)
		code2=re.sub('&#215;','',code1)
		code3=re.sub('&#038;','',code2)
		code4=re.sub('&#8216;','',code3)
		code5=re.sub('&#8217;','',code4)
		code6=re.sub('&#8211;','',code5)
		code7=re.sub('&#8220;','',code6)
		code8=re.sub('&#8221;','',code7)
		code9=re.sub('&#8212;','',code8)
    		code10=re.sub('&amp;','&',code9)
        	code11=re.sub("`",'',code10)
		match=re.compile('"cmsid">(.+?)</div><div style="display:none;" class="item-type">video</div><div style="display:none;" class="screenshot">.+?</div><a title="(.+?)" href=".+?".+?<img alt=".+?" border=".+?" height=".+?" width=".+?" src="(.+?)"').findall(code11)
		for url,name,thumb in match:
			addDir(name.replace('&amp;','&'),'http://www.nick.com/dynamo/video/data/mrssGen.jhtml?type=network&hub=home&loc=default&mode=episode&dartSite=nick.nol&mgid=mgid:cms:episode:spongebob.com:'+ url +'&demo=null&block=true',5,thumb,'')
		i=0
		for i in range (i+19):
			refer=openfile(referer)
			pagenumber = str(21*i+21)
		addDir('Page '+str(i+2),'http://www.nick.com/ajax/videos/'+refer+'-videos?_&sort=date+desc&start='+pagenumber+'&page=1&type=videoItem',3,'','')

def EPISODESNEWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req).read()
	code=re.sub('&quot;','',response)
	code1=re.sub('&#039;','',code)
	code2=re.sub('&#215;','',code1)
	code3=re.sub('&#038;','',code2)
	code4=re.sub('&#8216;','',code3)
	code5=re.sub('&#8217;','',code4)
	code6=re.sub('&#8211;','',code5)
	code7=re.sub('&#8220;','',code6)
	code8=re.sub('&#8221;','',code7)
	code9=re.sub('&#8212;','',code8)
    	code10=re.sub('&amp;','&',code9)
        code11=re.sub("`",'',code10)
	match=re.compile('"cmsid">(.+?)</div><div style="display:none;" class="item-type">video</div><div style="display:none;" class="screenshot">.+?</div><a title="(.+?)" href=".+?".+?<img alt=".+?" border=".+?" height=".+?" width=".+?" src="(.+?)"').findall(code11)
	for url,name,thumb in match:
		addDir(name.replace('&amp;','&'),'http://www.nick.com/dynamo/video/data/mrssGen.jhtml?type=network&hub=home&loc=default&mode=episode&dartSite=nick.nol&mgid=mgid:cms:video:nick.com:'+ url +'&demo=null&block=false',9,thumb,'')

def EPISODES(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req).read()
	code=re.sub('&quot;','',response)
	code1=re.sub('&#039;','',code)
	code2=re.sub('&#215;','',code1)
	code3=re.sub('&#038;','',code2)
	code4=re.sub('&#8216;','',code3)
	code5=re.sub('&#8217;','',code4)
	code6=re.sub('&#8211;','',code5)
	code7=re.sub('&#8220;','',code6)
	code8=re.sub('&#8221;','',code7)
	code9=re.sub('&#8212;','',code8)
    	code10=re.sub('&amp;','&',code9)
        code11=re.sub("`",'',code10)
	match=re.compile('"cmsid">(.+?)</div><div style="display:none;" class="item-type">video</div><div style="display:none;" class="screenshot">.+?</div><a title="(.+?)" href=".+?".+?<img alt=".+?" border=".+?" height=".+?" width=".+?" src="(.+?)"').findall(code11)
	for url,name,thumb in match:
		addDir(name.replace('&amp;','&'),'http://www.nick.com/dynamo/video/data/mrssGen.jhtml?type=network&hub=home&loc=default&mode=episode&dartSite=nick.nol&mgid=mgid:cms:episode:spongebob.com:'+ url +'&demo=null&block=false',5,thumb,'')

def SUBNEWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req).read()
	code=re.sub('&quot;','',response)
	code1=re.sub('&#039;','',code)
	code2=re.sub('&#215;','',code1)
	code3=re.sub('&#038;','',code2)
	code4=re.sub('&#8216;','',code3)
	code5=re.sub('&#8217;','',code4)
	code6=re.sub('&#8211;','',code5)
	code7=re.sub('&#8220;','',code6)
	code8=re.sub('&#8221;','',code7)
	code9=re.sub('&#8212;','',code8)
    	code10=re.sub('&amp;','&',code9)
        code11=re.sub("`",'',code10)
        names = re.compile('<media:title>(.+?)</media:title>').findall(code11)
        thumbs = re.compile('url="(.+?)jpg"').findall(code11)
        urls = re.compile('<media:player url="http://media.nick.com/mgid:cms:video:nick.com:(.+?)"/>').findall(code11)
	videos = [(names[i],thumbs[i],urls[i])for i in range (0,len(thumbs))]
	for name,thumb,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.nick.com/dynamo/video/data/mediaGen.jhtml?mgid=mgid:cms:video:nick.com:'+url+'&block=false&type=network',name)+"&mode="+str(6)
                item=xbmcgui.ListItem(name.replace('&amp;','&'), thumbnailImage=thumb+'.jpg')
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)


def SUB(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req).read()
	code=re.sub('&quot;','',response)
	code1=re.sub('&#039;','',code)
	code2=re.sub('&#215;','',code1)
	code3=re.sub('&#038;','',code2)
	code4=re.sub('&#8216;','',code3)
	code5=re.sub('&#8217;','',code4)
	code6=re.sub('&#8211;','',code5)
	code7=re.sub('&#8220;','',code6)
	code8=re.sub('&#8221;','',code7)
	code9=re.sub('&#8212;','',code8)
    	code10=re.sub('&amp;','&',code9)
        code11=re.sub("`",'',code10)
        names = re.compile('<media:title>(.+?)</media:title>').findall(code11)
        thumbs = re.compile('url="(.+?)jpg"').findall(code11)
        urls = re.compile('<media:player url="http://media.nick.com/mgid:cms:video:spongebob.com:(.+?)"/>').findall(code11)
	videos = [(names[i],thumbs[i],urls[i])for i in range (0,len(thumbs))]
	for name,thumb,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.nick.com/dynamo/video/data/mediaGen.jhtml?mgid=mgid:cms:video:spongebob.com:'+url+'&block=false&type=network',name)+"&mode="+str(6)
                item=xbmcgui.ListItem(name.replace('&amp;','&'), thumbnailImage=thumb+'.jpg')
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def PLAY(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
	if link.find('video/x-flv')<0:
		finalurl=re.compile('<src>(.+?)</src>\n</rendition>\n<rendition cdn=".+?" duration=".+?" bitrate=".+?" width=".+?" height=".+?"\ntype="video/mp4">').findall(link)[-1]
     		item = xbmcgui.ListItem(path=finalurl)
        	xbmcplugin.setResolvedUrl(pluginhandle, True, item)
	else:
		swap=re.compile('<src>(.+?)</src>\n</rendition>\n<rendition cdn=".+?" duration=".+?" bitrate=".+?" width=".+?" height=".+?"\ntype="video/x-flv">').findall(link)
		if not swap: swap=re.compile('<src>(.+?)</src>').findall(link)
     		item = xbmcgui.ListItem(path=swap[0])
        	xbmcplugin.setResolvedUrl(pluginhandle, True, item)

def PLAYJR(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	finalurl=re.compile('src>(.+?)</src>').findall(link)[0]
     	item = xbmcgui.ListItem(path=finalurl)
        xbmcplugin.setResolvedUrl(pluginhandle, True, item)

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def addDir(name,url,mode,thumbnail,plot=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name,
                                                "plot": plot} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

      
def addLink(name,url,iconimage,plot,date):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setInfo( type="Video", infoLabels={ "Plot": plot} )
        liz.setInfo( type="Video", infoLabels={ "Date": date} )
	liz.setProperty("IsPlayable","true");
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok

params=get_params()
url=None
name=None
mode=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
if mode==None or url==None or len(url)<1:
        print "categories"
        CATS()
elif mode==1:
        print "PAGE"
        SHOWS(url)
elif mode==2:
        print "PAGE"
        CATSPONGE(url)
elif mode==3:
        print "PAGE"
        CLIPS(url)
elif mode==4:
        print "PAGE"
        EPISODES(url)
elif mode==5:
        print "PAGE"
        SUB(url)
elif mode==6:
        print "PAGE"
        PLAY(url)
elif mode==7:
        print "PAGE"
        CLIPSNEWS(url)
elif mode==8:
        print "PAGE"
        EPISODESNEWS(url)
elif mode==9:
        print "PAGE"
        SUBNEWS(url)
elif mode==10:
        print "PAGE"
        SHOWSJR(url)
elif mode==11:
        print "PAGE"
        CHANNELS(url)
elif mode==12:
        print "PAGE"
        SUBSHOWS(url)
elif mode==13:
        print "PAGE"
        SUBCHANNELS(url)
elif mode==14:
        print "PAGE"
        CATSJR()
elif mode==15:
        print "PAGE"
        PLAYJR(url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))