#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit =
  val ls   = stdin.getLines().toList
  val ns   = ls.head.split(',').map(_.toInt).toList
  val bs   = ls.tail.flatMap(_.split(' ')).filter(_!="").map(_.toInt)
  val brd  = (bs: List[Int], i:Int) => bs.slice(i*25, (i+1)*25)
  val idx  = (v:Int) => bs.zipWithIndex.filter(_._1==v).map((_,i)=>i)
  val updt = (v:List[Int], js:List[Int]) => js.foldLeft(v)((a,i)=>a.updated(i, -a(i).abs))
  val play = ns.scanLeft(bs)((v,n)=>updt(v, idx(n))).tail
  val ii   = List(0,1,2,3,4)
  val rs   = ii.map(i=>ii.map(j=>i*5+j)).concat(ii.map(i=>ii.map(j=>j*5+i)))
  val win  = (xs:List[Int],o:Int) => rs.exists(_.map(-xs(_)).forall(ns.slice(0,o+1).contains))
  val when = (i:Int) => play.zipWithIndex.map((xs,j)=>if win(brd(xs,i),j) then 0 else 1).sum
  val stat = (i:Int, j:Int) => (j, ns(j) * brd(play(j), i).filter(_>0).sum)
  val ps   = (0 to -1 + bs.size/25).map(i=>stat(i, when(i))).sortBy((i,_)=>i)

  println(s"Part 1: ${ ps.head._2 }, Part 2: ${ ps.last._2 }")
