import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,cookielib,xbmcaddon
import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import feedparser


#TopDocs - nixa

def CATS():
        addDir('Science','http://topdocumentaryfilms.com/category/science-technology/page1',1,'')
 	addDir('Biography','http://topdocumentaryfilms.com/category/biography/page1',1,'')
 	addDir('Conspiracy','http://topdocumentaryfilms.com/category/crime-conspiracy/page1',1,'')
 	addDir('Environment','http://topdocumentaryfilms.com/category/environment/page1',1,'')
 	addDir('History','http://topdocumentaryfilms.com/category/history/page1',1,'')
 	addDir('Sports','http://topdocumentaryfilms.com/category/sports/page1',1,'')
 	addDir('Politics','http://topdocumentaryfilms.com/category/politics/page1',1,'')
 	addDir('Arts','http://topdocumentaryfilms.com/category/music-performing-arts/page1',1,'')
 	addDir('Drugs','http://topdocumentaryfilms.com/category/drugs/page1',1,'')
	addDir('Mystery','http://topdocumentaryfilms.com/category/mystery/page1',1,'')
	addDir('Military War','http://topdocumentaryfilms.com/category/military-war/page1',1,'')
	addDir('Nature','http://topdocumentaryfilms.com/category/nature-wildlife/page1',1,'')
	addDir('Sexuality','http://topdocumentaryfilms.com/category/sex/page1',1,'')
	addDir('Comedy','http://topdocumentaryfilms.com/category/comedy/page1',1,'')
	addDir('Philosophy','http://topdocumentaryfilms.com/category/philosophy/page1',1,'')
	addDir('Artists','http://topdocumentaryfilms.com/category/art-artists/page1',1,'')	
	addDir('Technology','http://topdocumentaryfilms.com/category/technology/page1',1,'')
	addDir('Economics','http://topdocumentaryfilms.com/category/economics/page1',1,'')
	addDir('Health','http://topdocumentaryfilms.com/category/health/page1',1,'')
	addDir('Media','http://topdocumentaryfilms.com/category/media/page1',1,'')
	addDir('Performing Arts','http://topdocumentaryfilms.com/category/music-performing-arts/page1',1,'')
	addDir('Psychology','http://topdocumentaryfilms.com/category/psychology/page1',1,'')
	addDir('Society','http://topdocumentaryfilms.com/category/society/page1',1,'')
	addDir('Recently added','http://topdocumentaryfilms.com/all/',3,'')
	addDir('Featured documentaries','http://topdocumentaryfilms.com/',4,'')
	addDir('Most commented documentaries','http://topdocumentaryfilms.com/most-commented-documentaries/',10,'')
	addDir('List All','http://topdocumentaryfilms.com/watch-online/',8,'')
	addDir('Search','http://topdocumentaryfilms.com/',9,'')

def LIST(url):
        		req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
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
                       	lexus=re.compile('href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></ul><ul><a').findall(code11)
			for url,name in lexus:
				addDir(name,url,2,'','')
	     
def INDEX(url):
        		req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
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
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img\nsrc="(.+?)" alt=".+?" align="left" /></a>(.+?)</p><p\n').findall(code11)
                       	nxt=re.compile('href="(.+?)">Next</a></div></div><div').findall(code11)
			for url,name,thumb,plot in lexus:
				addDir(name,url,2,thumb,plot)
			for url in nxt:
				addDir('Next',url,1,'http://www.nws.noaa.gov/os/marine/safeboating/monday_files/next.gif','')

def INDEX2(url):
                        req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
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
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img').findall(code11)
                        for url,name in lexus:
				addDir(name,url,2,'','')

def INDEX3(url):
                        req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
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
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img').findall(code11)
                        for url,name in lexus:
				addDir(name,url,2,'','')

def INDEX4(url):
                        req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
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
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img').findall(code11)
                        for url,name in lexus:
				addDir(name,url,2,'','')

def VIDS(url,name):
	i=0
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link=response.read()
	altcode=re.compile('href="http://www.youtube.com/view_play_list(.+?)"').findall(link)
	for code in altcode:
		req = urllib2.Request("http://gdata.youtube.com/feeds/api/playlists/"+code.replace('?p=','')+"?&v=2&max-results=50")
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req)
		link=response.read()
		urlsingle = re.compile("part</media:keywords><media:player url='(.+?)'/><media:thumbnail").findall(link)
		urlsingle2 = re.compile("</title><link rel='alternate' type='text/html' href='(.+?)'").findall(link)
		for url in urlsingle:
			try:
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				link = response.read()
				finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
				#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        			#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),item)
				i=i+1
				addLink('Play '+name.replace(' ','')+' -'+' Part '+ str(i),'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')
			except: pass
		for url in urlsingle2:
			try:
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				link = response.read()
				finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
				#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        			#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),item)
				i=i+1
				addLink('Play '+name.replace(' ','')+' -'+' Part '+ str(i),'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')
			except: pass

	try:
		coderaw=re.compile('value="http://www.youtube.com/p/(.+?)"').findall(link)[0]
		codeplist = coderaw[:16]
		match="http://gdata.youtube.com/feeds/api/playlists/"+codeplist+"?&v=2&max-results=50"
		req = urllib2.Request(match)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req)
		link=response.read()
		urlsingle = re.compile("part</media:keywords><media:player url='(.+?)'/><media:thumbnail").findall(link)
		urlsingle2 = re.compile("</title><link rel='alternate' type='text/html' href='(.+?)'").findall(link)
		for url in urlsingle:
			try:
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				link = response.read()
				finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
				#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        			#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),item)
				i=i+1
				addLink('Play '+name.replace(' ','')+' -'+' Part '+ str(i),'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')
			except: pass
		for url in urlsingle2:
			try:
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				link = response.read()
				finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
				#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        			#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),item)
				i=i+1
				addLink('Play '+name.replace(' ','')+' -'+' Part '+ str(i),'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')
			except: pass
	except: pass

	try:
		coderaw2=re.compile('value="http://www.youtube.com/v/(.+?)"').findall(link)[0]
		codeplist2 = coderaw2[:11]
		req = urllib2.Request('http://www.youtube.com/watch?v='+codeplist2)
		response = urllib2.urlopen(req)
		link = response.read()
		finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
		#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        	#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),item)
		addLink('Play '+name,'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')

	except: pass

	try:
      		gubacode=re.compile("src='http://www.guba.com/.+?bid=(.+?)' quality='.+?'").findall(link)[0]
		flvpath="http://www.guba.com/playerConfig?isEmbeddedPlayer=true&bid="+gubacode
		req = urllib2.Request(flvpath)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req);
		link=response.read()
		match = re.compile('"url":"(.+?)?mt').findall(link)
    		for url in match:
                	addLink('Play (guba) '+name,url,'','','')
	except: pass

	try:
		blp=re.compile('src="http://blip.tv/play/(.+?)"').findall(link)
		for code in blp:
			req = urllib2.Request('http://www.flashvideodownloader.org/download2.php?u=http://blip.tv/play/'+code)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		page = urllib2.urlopen(req);new=page.read();page.close()
        		dw=re.compile('<p>Click Here to download </a></p><a href="(.+?)"').findall(new)
        		for url in dw:
				addLink('Play '+name,url,'','','')
	except: pass

	try:
		blp=re.compile('value="file=(.+?)flv').findall(link)[0]
		addLink('Play '+name,'http://server1.sureynot.com/xmoov.php?file='+blp+'flv','','','')

	except: pass

	try:
		vid=re.compile('"http://videos.engagemedia.org/(.+?)"').findall(link)[0]
		addLink('Play '+name+ '(Full)','http://videos.engagemedia.org/'+vid,'','','')

	except: pass

	try:
		vid=re.compile('clip_id=(.+?)&amp;server=vimeo').findall(link)[0]
		code='http://www.flashvideodownloader.org/download2.php?u=http://vimeo.com/'+vid
		print code
		req = urllib2.Request(code)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	req.add_header('Referer', 'http://www.flashvideodownloader.org/')
        	page = urllib2.urlopen(req);new=page.read();page.close()
		dw=re.compile('http://av.vimeo.com/(.+?)\n').findall(new)[0]
		addLink('Play '+name+ '(Full)','http://av.vimeo.com/'+dw,'','','')

	except: pass

	try:
		vid=re.compile('value="http://www.dailymotion.com/swf/video/(.+?)?additionalInfos=0"').findall(link)
		for url in vid:
			i=i+1
			addDir(name +' -'+' Part '+ str(i),'http://www.dailymotion.com/video/'+url.replace('?','')+'#from=embed',7,'','')
	except: pass

	try:
		swap=re.compile('src=".+?docId=(.+?)"').findall(link)
		if not swap: swap=re.compile('<embed style=".+?" id=".+?" type="application/x-shockwave-flash" src=".+?docId=(.+?)" allowFullScreen="true"').findall(link)
		if not swap: swap=re.compile('src=".+?docid=(.+?)&#038;hl=un"').findall(link)
		if not swap: swap=re.compile('src=".+?docid=(.+?)&#038;hl=en"').findall(link)
		if not swap: swap=re.compile('src=.+?docid=(.+?)&#038;hl=en&#038;fs=true').findall(link)
		for code in swap:
			try:
				req = urllib2.Request('http://video.google.com/videofeed?fgvns=1&fai=1&docid='+code+'&hl=undefined')
				response = urllib2.urlopen(req)
				link2 = response.read()
        			dw=re.compile('content url="(.+?)" type="video/x-flv"').findall(link2)[0]
				addLink('Play '+name,dw.replace('amp;',''),'','','')
			except: pass
	except: pass

       	try:
                megavideo=re.compile('name="movie" value="http://www.megavideo.com/v/(.+?)"></param>').findall(link)
               	mvid = megavideo[0]
                mvid = mvid[0:8]
                req = urllib2.Request("http://www.megavideo.com/xml/videolink.php?v="+mvid)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                req.add_header('Referer', 'http://www.megavideo.com/')
                lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
                errort = re.compile(' errortext="(.+?)"').findall(response)
                if len(errort) > 0: addLink(errort[0],'http://novid.com','')
                else:
                        s = re.compile(' s="(.+?)"').findall(response)
                        k1 = re.compile(' k1="(.+?)"').findall(response)
                        k2 = re.compile(' k2="(.+?)"').findall(response)
                        un = re.compile(' un="(.+?)"').findall(response)
                        movielink = "http://www" + s[0] + ".megavideo.com/files/" + decrypt(un[0], k1[0], k2[0]) + "/"
                        addLink('Play '+name, movielink+'?.flv','')
        except: pass



def PLAYDM(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link = response.read()
		finalurl=re.compile('"video", "http://www.dailymotion.com/cdn/(.+?)"').findall(link)[0]
		#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        	#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://www.dailymotion.com/cdn/'+finalurl,item)
		addLink('Play '+name,'http://www.dailymotion.com/cdn/'+finalurl,'','','')

def PLAY(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link = response.read()
		finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
		#item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        	#ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play('http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),item)
		addLink('Play '+name,'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')

def AltYoutube(url):
		i=0
		req = urllib2.Request(url)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req)
		link=response.read()
		urlsingle = re.compile("part</media:keywords><media:player url='(.+?)'/><media:thumbnail").findall(link)
		urlsingle2 = re.compile("</title><link rel='alternate' type='text/html' href='(.+?)'").findall(link)
		for url in urlsingle:
			i=i+1
			addDir('Play '+name.replace(' ','')+' -'+' Part '+ str(i),url,5,'','')
		for url in urlsingle2:
			i=i+1
			addDir('Play '+name.replace(' ','')+' -'+' Part '+ str(i),url,5,'','')

def PLAYRARE(url):

		req = urllib2.Request(url)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req);
		link=response.read()
		codeplist=re.compile('<link rel="canonical" href="/watch?v=(.+?)">').findall(link)[0]
		match="http://www.youtube.com/watch?v="+codeplist
		print match
		req = urllib2.Request(match)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req);
		link=response.read()
		hqvid=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)
		for url in hqvid:
			addLink('Play '+name,'http://'+url.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')

def GOOGLE(url):

			req = urllib2.Request(url)
			response = urllib2.urlopen(req)
			link2 = response.read()
        		dw=re.compile('content url="(.+?)" type="video/x-flv"').findall(link2)[0]
			item = xbmcgui.ListItem(name.replace('(xtshare)',''))
        		ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(dw.replace('amp;',''),item)
			addLink('Play '+name,url.replace('amp;',''),'','','')


def SEARCH():
        keyb = xbmc.Keyboard('', 'Search TopDocumentaryFilms')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
		sURL = 'http://www.google.com/cse?cx=partner-pub-2600122794880266%3Auqpjg8s2z8l&cof=FORID%3A11&ie=UTF-8&q='+encode+'&sa=Search&ad=w9&num=150&rurl=http://topdocumentaryfilms.com/search/?cx=partner-pub-2600122794880266%3Auqpjg8s2z8l&cof=FORID%3A11&ie=UTF-8&q='+encode+'&sa=Search'
		user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
		req = urllib2.Request(sURL)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link = response.read()
		match=re.compile('class=r><a href="(.+?)" target=_top class=l onmousedown=".+?">(.+?)Watch Free Documentary Online').findall(link)
		nxt=re.compile('<a href="(.+?)"><span>Next</span>').findall(link)
		for url,name in match:
			addDir(name.replace('<em>','').replace('</em>','').replace('|','').replace('&#039;',''),url,2,'','')
def ajoin(arr):
    strtest = ''
    for num in range(len(arr)):
        strtest = strtest + str(arr[num])
    return strtest

def asplit(mystring):
    arr = []
    for num in range(len(mystring)):
        arr.append(mystring[num])
    return arr
	
def decrypt(str1, key1, key2):

    __reg1 = []
    __reg3 = 0
    while (__reg3 < len(str1)):
        __reg0 = str1[__reg3]
        holder = __reg0
        if (holder == "0"):
            __reg1.append("0000")
        else:
            if (__reg0 == "1"):
                __reg1.append("0001")
            else:
                if (__reg0 == "2"): 
                    __reg1.append("0010")
                else: 
                    if (__reg0 == "3"):
                        __reg1.append("0011")
                    else: 
                        if (__reg0 == "4"):
                            __reg1.append("0100")
                        else: 
                            if (__reg0 == "5"):
                                __reg1.append("0101")
                            else: 
                                if (__reg0 == "6"):
                                    __reg1.append("0110")
                                else: 
                                    if (__reg0 == "7"):
                                        __reg1.append("0111")
                                    else: 
                                        if (__reg0 == "8"):
                                            __reg1.append("1000")
                                        else: 
                                            if (__reg0 == "9"):
                                                __reg1.append("1001")
                                            else: 
                                                if (__reg0 == "a"):
                                                    __reg1.append("1010")
                                                else: 
                                                    if (__reg0 == "b"):
                                                        __reg1.append("1011")
                                                    else: 
                                                        if (__reg0 == "c"):
                                                            __reg1.append("1100")
                                                        else: 
                                                            if (__reg0 == "d"):
                                                                __reg1.append("1101")
                                                            else: 
                                                                if (__reg0 == "e"):
                                                                    __reg1.append("1110")
                                                                else: 
                                                                    if (__reg0 == "f"):
                                                                        __reg1.append("1111")

        __reg3 = __reg3 + 1

    mtstr = ajoin(__reg1)
    __reg1 = asplit(mtstr)
    __reg6 = []
    __reg3 = 0
    while (__reg3 < 384):
    
        key1 = (int(key1) * 11 + 77213) % 81371
        key2 = (int(key2) * 17 + 92717) % 192811
        __reg6.append((int(key1) + int(key2)) % 128)
        __reg3 = __reg3 + 1
    
    __reg3 = 256
    while (__reg3 >= 0):

        __reg5 = __reg6[__reg3]
        __reg4 = __reg3 % 128
        __reg8 = __reg1[__reg5]
        __reg1[__reg5] = __reg1[__reg4]
        __reg1[__reg4] = __reg8
        __reg3 = __reg3 - 1
    
    __reg3 = 0
    while (__reg3 < 128):
    
        __reg1[__reg3] = int(__reg1[__reg3]) ^ int(__reg6[__reg3 + 256]) & 1
        __reg3 = __reg3 + 1

    __reg12 = ajoin(__reg1)
    __reg7 = []
    __reg3 = 0
    while (__reg3 < len(__reg12)):

        __reg9 = __reg12[__reg3:__reg3 + 4]
        __reg7.append(__reg9)
        __reg3 = __reg3 + 4
        
    
    __reg2 = []
    __reg3 = 0
    while (__reg3 < len(__reg7)):
        __reg0 = __reg7[__reg3]
        holder2 = __reg0
    
        if (holder2 == "0000"):
            __reg2.append("0")
        else: 
            if (__reg0 == "0001"):
                __reg2.append("1")
            else: 
                if (__reg0 == "0010"):
                    __reg2.append("2")
                else: 
                    if (__reg0 == "0011"):
                        __reg2.append("3")
                    else: 
                        if (__reg0 == "0100"):
                            __reg2.append("4")
                        else: 
                            if (__reg0 == "0101"): 
                                __reg2.append("5")
                            else: 
                                if (__reg0 == "0110"): 
                                    __reg2.append("6")
                                else: 
                                    if (__reg0 == "0111"): 
                                        __reg2.append("7")
                                    else: 
                                        if (__reg0 == "1000"): 
                                            __reg2.append("8")
                                        else: 
                                            if (__reg0 == "1001"): 
                                                __reg2.append("9")
                                            else: 
                                                if (__reg0 == "1010"): 
                                                    __reg2.append("a")
                                                else: 
                                                    if (__reg0 == "1011"): 
                                                        __reg2.append("b")
                                                    else: 
                                                        if (__reg0 == "1100"): 
                                                            __reg2.append("c")
                                                        else: 
                                                            if (__reg0 == "1101"): 
                                                                __reg2.append("d")
                                                            else: 
                                                                if (__reg0 == "1110"): 
                                                                    __reg2.append("e")
                                                                else: 
                                                                    if (__reg0 == "1111"): 
                                                                        __reg2.append("f")
                                                                    
        __reg3 = __reg3 + 1

    endstr = ajoin(__reg2)
    return endstr

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
        INDEX(url)
elif mode==2:
        print "PAGE"
        VIDS(url,name)
elif mode==3:
        print "PAGE"
        INDEX2(url)
elif mode==4:
        print "PAGE"
        INDEX3(url)
elif mode==10:
        print "PAGE"
        INDEX4(url)
elif mode==5:
        print "PAGE"
        PLAY(url)
elif mode==6:
        print "PAGE"
        PLAYRARE(url)
elif mode==7:
        print "PAGE"
        PLAYDM(url)
elif mode==8:
        print "LIST"
        LIST(url)
elif mode==9:
        print "SEARCH  :"+url
        SEARCH()
elif mode==11:
        print "PAGE"
        AltYoutube(url)
elif mode==12:
        print "PAGE"
        GOOGLE(url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
