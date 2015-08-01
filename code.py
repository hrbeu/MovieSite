#-*- coding:utf-8 -*-
import web

urls=(
      '/','index',
      '/movie/(\d+)','movie',
      '/cast/(.*)','cast',
      '/director/(.*)','director',
      )

render=web.template.render('D:/webpy test/templates/')
db=web.database(dbn='sqlite',db='D:/sqlite/MovieSite.db')

class index:
     def GET(self):
          movies=db.select('movie')
          statement='SELECT COUNT(*) AS COUNT FROM movie'
          count=db.query(statement)[0]['COUNT']
          return render.index(movies,count,None)
     def POST(self):
          data=web.input()
          condition=r'title like "%'+data.title+r'%"'
          movies=db.select('movie',where=condition)
          statement='SELECT COUNT(*) AS COUNT FROM movie WHERE '+condition
          result=db.query(statement)
          print result
          result_one=result[0]
          print result_one
          count=result_one['COUNT']
          return render.index(movies,count,data.title)
     
class movie:
     def GET(self,movie_id):
          movie_id=int(movie_id)
          movie=db.select('movie',where='id=$movie_id',vars=locals())[0]
          return render.movie(movie)

class cast:
     def GET(self,cast_name):
          condition=r'casts like "%'+cast_name +r'%"'
          movies=db.select('movie',where=condition)
          statement='SELECT COUNT(*)  FROM movie  WHERE '+condition
          count=db.query(statement)[0]['COUNT(*)']
          return render.index(movies,count,cast_name)

class director:
      def GET(self,director_name):
          condition=r'directors like "%'+director_name+r'%"'
          movies=db.select('movie',where=condition)
          statement='SELECT COUNT(*) AS COUNT FROM movie WHERE '+condition
          count=db.query(statement)[0]['COUNT']
          return render.index(movies,count,director_name)
      
def notfound():
     return web.notfound("Sorry,the page you were looking for was not found.")

if __name__=="__main__":
	app=web.application(urls,globals())
	app.notfound=notfound
	app.run()
