#!/usr/bin/env scala
import scala.io.Source.stdin

type Chars = List[Char]

@main def aoc(): Unit = 
  val ns   = stdin.getLines().map(_.toList).toList
  val inv  = (xs:Chars) => xs.map(x=> if x == '1' then '0' else '1')
  val b2i  = (xs:Chars) => xs.foldLeft(0)((a,b)=> a*2 + (b-'0'))

  def fltr(xs: List[Chars], i:Int, f:Boolean=false):Chars = {
    xs.length match {
      case 1 => xs(0)
      case _ => val c = if f then ('0','1') else ('1','0')
                val v = if xs.map(_(i)).count(_=='1')<xs.length/2.0 then c(0) else c(1)
                fltr(xs.filter(_(i)==v), i+1, f) }}

  val p1   = ns.transpose.map(xs=>if xs.count(_=='1')<xs.length/2.0 then '0' else '1')
  val p2   = b2i(fltr(ns, 0)) * b2i(fltr(ns, 0, true))

  println(s"Part 1: ${ b2i(p1) * b2i(inv(p1)) }, Part 2: ${ p2 }")