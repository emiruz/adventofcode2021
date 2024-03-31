#!/usr/bin/env scala
import scala.io.Source.stdin

def lines(a:Int, b:Int, c:Int, d:Int) =
  if (a==c)      (List(b,d).min to List(b,d).max).map((a,_))
  else if (b==d) (List(a,c).min to List(a,c).max).map((_,b))
  else            List()    

def diags(a:Int, b:Int, c:Int, d:Int) =
  val (dx, dy) = (if a<c then 1 else -1, if b<d then 1 else -1)
  val l = List((c-a).abs, (d-b).abs).max
  if (a==c || b==d) List()
  else             (0 to l).map(i=>(a+i*dx, b+i*dy))

@main def aoc(): Unit =
  val ls   = stdin.getLines().map(("\\d+".r).findAllIn(_)
             .map(_.toInt).toList).map(x=>(x(0),x(1),x(2),x(3))).toList
  val mx   = ls.map(_.toList.max).max + 1
  val updt = (v:Vector[Int], x:(Int,Int))=>
             { val i = x._1*mx+x._2; v.updated(i, v(i)+1) }
  val p1   = ls.flatMap(lines.tupled).foldLeft(Vector.fill(mx*mx)(0))(updt)
  val p2   = ls.flatMap(diags.tupled).foldLeft(p1)(updt)

  println(s"Part 1: ${ p1.count(_>1) }, Part 2: ${ p2.count(_>1) }")
