#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit =
  val ch = "abcdefg".toVector
  val ns = List("abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg").map(_.toSet)
  val xs = stdin.getLines().map(_.replace("| ","").split(" ").toList).toList
  val tr = (xs: String, p:IndexedSeq[Int]) => xs.map(x=>ch(p(ch.indexOf(x)))).toSet
  val pr = (xs:List[String], p:IndexedSeq[Int]) => xs.map(tr(_,p)).forall(ns.contains)
  val f  = (xs:List[String]) => (0 to 6).permutations.find(pr(xs,_)).get
  val ps = xs.map(x=>(x,f(x.dropRight(4)))).map((x,p)=>x.takeRight(4).map(i=>ns.indexOf(tr(i,p))))
  val p1 = ps.map(_.count(List(1,4,7,8).contains)).sum
  
  println(s"Part 1: ${ p1 }, Part 2: ${ ps.map(_.mkString.toInt).sum }")
