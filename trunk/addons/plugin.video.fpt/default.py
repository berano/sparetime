import urllib,urllib2,re,sys,xbmcplugin,xbmcgui
import cookielib,os,string,cookielib,StringIO
import os,time,base64
import xbmcaddon

fpt=xbmcaddon.Addon(id='plugin.video.fpt')


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

fptpath = 'special://profile/addon_data/plugin.video.fpt'
translatedfptpath = xbmcpath(fptpath,'')
referer = xbmcpath(fptpath,'ref.txt')

def CATS():
        addDir('Tv Shows','http://www.fastpasstv.com/tv',2,'')
        addDir('New Episodes Added','http://www.fastpasstv.com/tv',14,'')
        addDir('Latest Added Tv Shows','http://www.fastpasstv.com/',4,'')
        addDir('Latest Added Movies','http://www.fastpasstv.com/',5,'')
	addDir('Movies','http://www.fastpasstv.com/movies',1,'')
	#addDir('Documentaries','http://www.fastpasstv.com/documentaries',1,'')
	addDir('Search','http://www.fastpasstv.com/',9,'')

def NEWEP(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
     	listnew=re.compile('<li><a href="(.+?)">(.+?)<font class="newvid">New Episodes!').findall(link)
	for url,name in listnew:
		addDir(name+' (NEW EPISODE!)','http://www.fastpasstv.com'+url,4,'')

def X1(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
     	mvs=re.compile('<li><a href="(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(link)
	for url,name in mvs:
		addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com'+url,6,'')

def X2(url,name): 
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
     	list=re.compile('<li><a href="(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(link)
	for url,name in list:
		addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com'+url,4,'')

def X3(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        link=response2.read()
        response2.close()
      	mvs=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
	for url,name in mvs:
		addDir(name,'http://www.fastpasstv.com'+url,18,'')

def Y1(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
      	tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)</a></li>').findall(link)
      	crt=re.compile('<li><a href="/cartoons/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in tvs:
		addDir(name,'http://www.fastpasstv.com/tv/'+url2,18,'')
	for url2,name in crt:
		addDir(name,'http://www.fastpasstv.com/cartoons/'+url2,18,'')

def Y2(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
      	mvs=re.compile('<li><a href="/movies/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in mvs:
		addDir(name,'http://www.fastpasstv.com/movies/'+url2,6,'')

def Y3MOV(url,name):
	i=0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        ref=response2.geturl()
	save(referer,ref)
        link=response2.read()
       	fv=re.compile('<b>.+?Flash.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	fv2=re.compile('<b>VidX.+?FLV.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	dv=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	dv1=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      	dv2=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      	vidbx=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	vidbx1=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      	vidbx2=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      	wise=re.compile('<b>WiseVid</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	for url in fv:
		i=i+1
		addDir('DivxDen (flv) #'+str(i),'http://www.fastpasstv.com'+url,7,'','')
	for url in fv2:
		i=i+1
		addDir('DivxDen (flv) #'+str(i),'http://www.fastpasstv.com'+url,7,'','')
	for url in dv1:
		i=i+1
		addDir('DivxDen (avi) Pt 1 #'+str(i),'http://www.fastpasstv.com'+url,8,'','')
	for url in dv2:
		i=i+1
		addDir('DivxDen (avi) Pt 2 #'+str(i),'http://www.fastpasstv.com'+url,8,'','')
	for url in dv:
		i=i+1
		addDir('DivxDen (avi) #'+str(i),'http://www.fastpasstv.com'+url,8,'','')
	for url in vidbx:
		i=i+1
		addDir('VidBux (avi) #'+str(i),'http://www.fastpasstv.com'+url,10,'','')
	for url in vidbx1:
		i=i+1
		addDir('VidBux (avi) Pt 1 #'+str(i),'http://www.fastpasstv.com'+url,10,'','')
	for url in vidbx2:
		i=i+1
		addDir('VidBux (avi) Pt 2 #'+str(i),'http://www.fastpasstv.com'+url,10,'','')
	for url in wise:
		i=i+1
		addDir('Wisevid #'+str(i),'http://www.fastpasstv.com'+url,19,'')

def Y3TV(url,name):
	i=0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        ref=response2.geturl()
	save(referer,ref)
        link=response2.read()
       	fv=re.compile('<b>.+?Flash.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	fv2=re.compile('<b>VidX.+?FLV.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	dv=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	dv1=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      	dv2=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      	vidbx=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
       	wise=re.compile('<b>WiseVid</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	for url in fv:
		i=i+1
		addDir('DivxDen (flv) #'+str(i),'http://www.fastpasstv.com'+url,7,'')
	for url in fv2:
		i=i+1
		addDir('DivxDen (flv) #'+str(i),'http://www.fastpasstv.com'+url,7,'','')
	for url in dv1:
		i=i+1
		addDir('DivxDen (avi) Pt 1 #'+str(i),'http://www.fastpasstv.com'+url,8,'')
	for url in dv2:
		i=i+1
		addDir('DivxDen (avi) Pt 2 #'+str(i),'http://www.fastpasstv.com'+url,8,'')
	for url in dv:
		i=i+1
		addDir('DivxDen (avi) #'+str(i),'http://www.fastpasstv.com'+url,8,'')
	for url in vidbx:
		i=i+1
		addDir('VidBux (avi) #'+str(i),'http://www.fastpasstv.com'+url,10,'','')
	for url in wise:
		i=i+1
		addDir('Wisevid #'+str(i),'http://www.fastpasstv.com'+url,19,'')

def VIDSFLV(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
 	values = {'login': uname,'password': pwd}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(urlogin, data, headers)
	response = urllib2.urlopen(req)
	
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()

    	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()
	fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link2)[0]
	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link2)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(gurl, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()
	item = xbmcgui.ListItem(name)

	file=re.compile("s(.+?)182|file").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-46:].replace(' ','')	
	hashshort =  re.compile('divxden(.+?)file').findall(link)[0]
    	finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:182/d/'+hashlong+'/'+ fcodenm
       	if (fpt.getSetting('download') == '0'):
                    dia = xbmcgui.Dialog()
                    ret = dia.select('Streaming Options', ['Play','Download'])
                    if (ret == 0):
		            ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		            addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
                    elif (ret == 1):
                            path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                            Download(finalurl,path+name+'.avi')
                    else:
                            return
	elif (fpt.getSetting('download') == '1'):
		ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
        elif (fpt.getSetting('download') == '2'):
                path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                Download(finalurl,path+name+'.avi')
        else:
        	return

def VIDSDIVX(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
 	values = {'login': uname,'password': pwd}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(urlogin, data, headers)
	response = urllib2.urlopen(req)

        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()

      	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()
	fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link2)[0]
	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link2)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(gurl, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("pluginspage(.+?)video").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-46:].replace(' ','')
	rawhashshort = re.compile('divxden(.+?)np_vid').findall(link)[0]
	hashshort =  re.compile('divxden(.+?)src').findall(link)[0]
   	finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:182/d/'+hashlong+'/'+ fcodenm
        if (fpt.getSetting('download') == '0'):
                    dia = xbmcgui.Dialog()
                    ret = dia.select('Streaming Options', ['Play','Download'])
                    if (ret == 0):
	            	    ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		            addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
                    elif (ret == 1):
                            path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                            Download(finalurl,path+name+'.avi')
                    else:
                            return
	elif (fpt.getSetting('download') == '1'):
		ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
        elif (fpt.getSetting('download') == '2'):
                path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                Download(finalurl,path+name+'.avi')
        else:
        	return

def VIDBUX(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
 	values = {'login': uname,'password': pwd}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(urlogin, data, headers)
	response = urllib2.urlopen(req)

        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()

      	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()
	fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link2)[0]
	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link2)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(gurl, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("custommode(.+?)182|file").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-41:].replace(' ','')
	hashshort =  re.compile('</div><!-- <img src="http://(.+?).vidbux.com').findall(link)[0]
   	finalurl = 'http://'+hashshort+'.vidbux.com:182/d/'+hashlong+'/'+ fcodenm
        if (fpt.getSetting('download') == '0'):
                    dia = xbmcgui.Dialog()
                    ret = dia.select('Streaming Options', ['Play','Download'])
                    if (ret == 0):
		            ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		            addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
                    elif (ret == 1):
                            path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                            Download(finalurl,path+name+'.avi')
                    else:
                            return
	elif (fpt.getSetting('download') == '1'):
		ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
        elif (fpt.getSetting('download') == '2'):
                path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                Download(finalurl,path+name+'.avi')
        else:
        	return


def SEARCH():
        keyb = xbmc.Keyboard('', 'Search FASTPASSTV')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
		values = {'input': encode,'submit': 'Search'}
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = { 'User-Agent' : user_agent }
		data = urllib.urlencode(values)
                req = urllib2.Request('http://www.fastpasstv.com/search',data,headers)
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req).read()
     		tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(response)
     		docs=re.compile('li><a href="/documentaries/(.+?)">(.+?)<span class="epnum"').findall(response)
     		ctn=re.compile('<li><a href="/cartoons/(.+?)">(.+?)<span class="epnum">.+?</span></a>').findall(response)
     		mvs=re.compile('<li><a href="/movies/(.+?)">(.+?)<span class="epnum">.+?</span></a>').findall(response)
		for url,name in tvs:
			addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com/tv/'+url,4,'')
		for url,name in ctn:
			addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com/cartoons/'+url,4,'')
		for url,name in mvs:
			addDir(name,'http://www.fastpasstv.com/movies/'+url,6,'')
		for url,name in docs:
			addDir(name,'http://www.fastpasstv.com/documentaries/'+url,6,'')

def WISE(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
 	values = {'login': uname,'password': pwd}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(urlogin, data, headers)
	response = urllib2.urlopen(req)
	#Redirect
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()

      	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()

	try:
			rawcode=re.compile("javascript:location.href='(.+?)'").findall(link2)[1]
			code=rawcode.replace('http://www.wisevid.com/play?v=','')
			ref=response.geturl()
			values = {'name': 'no','value': 'Yes, let me watch'}
			user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
			headers = { 'User-Agent' : user_agent, 'Referer': ref}
			data = urllib.urlencode(values)
			req = urllib2.Request(rawcode, data, headers)
			response = urllib2.urlopen(req)
			link = response.read()
			match=re.compile("getF(\(.+?)'").findall(link)[0]
			clean= match.replace("('","")
			finalurl=base64.decodestring(clean)
       			if (fpt.getSetting('download') == '0'):
                    		dia = xbmcgui.Dialog()
                    		ret = dia.select('Streaming Options', ['Play','Download'])
                    		if (ret == 0):
		            		ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		            		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
                    		elif (ret == 1):
                            		path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                            		Download(finalurl,path+name+'.avi')
                    		else:
                            		return
			elif (fpt.getSetting('download') == '1'):
				ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
				addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
        		elif (fpt.getSetting('download') == '2'):
                		path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                		Download(finalurl,path+name+'.avi')
        		else:
        			return
	except: pass

	try:
			acode=re.compile('<input type="hidden" name="a" value="(.+?)" />').findall(link2)[0]
			vcode=re.compile('<input type="hidden" name="v" value="(.+?)" />').findall(link2)[0]
			url2='http://www.wisevid.com/play?v='+vcode
			values = {'a': acode,'v': vcode, 'no1' : 'Yes, let me watch'}
			user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
			headers = { 'User-Agent' : user_agent, 'Referer': 'http://www.wisevid.com/gate-way?v='+vcode}
			data = urllib.urlencode(values)
			req = urllib2.Request(url2, data, headers)
			response = urllib2.urlopen(req)
			link = response.read()
			match=re.compile("getF(\(.+?)'").findall(link)[0]
			clean= match.replace("('","")
			finalurl=base64.decodestring(clean)
       			if (fpt.getSetting('download') == '0'):
                    		dia = xbmcgui.Dialog()
                    		ret = dia.select('Streaming Options', ['Play','Download'])
                    		if (ret == 0):
		            		ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
		            		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
                    		elif (ret == 1):
                            		path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                            		Download(finalurl,path+name+'.avi')
                    		else:
                            		return
			elif (fpt.getSetting('download') == '1'):
				ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, name)
				addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
        		elif (fpt.getSetting('download') == '2'):
                		path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                		Download(finalurl,path+name+'.avi')
        		else:
        			return
	except: pass

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

class StopDownloading(Exception): 
        def __init__(self, value): 
            self.value = value 
        def __str__(self): 
            return repr(self.value) 

def Download(url, dest): 
        dp = xbmcgui.DialogProgress() 
        dp.create('Downloading', '', name) 
        start_time = time.time() 
        try: 
            urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time)) 
        except: 
            #delete partially downloaded file 
            while os.path.exists(dest): 
                try: 
                    print 'hello' 
                    break 
                except: 
                     pass 
            #only handle StopDownloading (from cancel), ContentTooShort (from urlretrieve), and OS (from the race condition); let other exceptions bubble 
            if sys.exc_info()[0] in (urllib.ContentTooShortError, StopDownloading, OSError): 
                return 'false' 
            else: 
                raise 
        return 'downloaded' 
         
def _pbhook(numblocks, blocksize, filesize, dp, start_time): 
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            # print ( 
                # percent, 
                # numblocks, 
                # blocksize, 
                # filesize, 
                # currently_downloaded, 
                # kbps_speed, 
                # eta, 
                # ) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs, e) 
            #print percent, mbs, e 
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
            raise StopDownloading('Stopped Downloading') 
 
def addLink(name,url,iconimage,plot,date):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty("IsPlayable","true");
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok

def check_settings():
		uname = fpt.getSetting('uname')
		pwd   = fpt.getSetting('pwd')
		if (not uname or uname == '') or (not pwd or pwd == ''):
				d = xbmcgui.Dialog()
				d.ok('Welcome to fastpasstv.com', 'To start using this plugin first go to www.fastpasstv.com.','and create an (free) account.')
				fpt.openSettings(sys.argv[ 0 ]) 
						
params=get_params()
url=None
name=None
mode=None

check_settings()
uname = fpt.getSetting('uname')
pwd   = fpt.getSetting('pwd')

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
        X1(url,name)
elif mode==11:
        print "PAGE"
        ICE(url,name)
elif mode==2:
        print "PAGE"
        X2(url,name)
elif mode==3:
        print "PAGE"
        X3(url,name)
elif mode==4:
        print "PAGE"
        Y1(url,name)
elif mode==5:
        print "PAGE"
        Y2(url,name)
elif mode==6:
        print "PAGE"
        Y3MOV(url,name)
elif mode==7:
        print "PAGE"
        VIDSFLV(url,name)
elif mode==8:
        print "PAGE"
        VIDSDIVX(url,name)
elif mode==9:
        print "SEARCH  :"+url
        SEARCH()
elif mode==14:
        print "PAGE"
        NEWEP(url,name)
elif mode==18:
        print "PAGE"
        Y3TV(url,name)
elif mode==19:
        print "PAGE"
        WISE(url,name)
elif mode==10:
        print "PAGE"
        VIDBUX(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))