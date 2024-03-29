#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit = 
  val ns = stdin.getLines().map(_.split(' ')).map(x=>(x(0).head, x(1).toInt)).toList
  val f  = (k:Char,v:Int) => k match { case 'f'=>(v,0) case 'u'=>(0,-v) case 'd'=>(0,v) }
  val p1 = ns.map(f.tupled).reduce((a,b)=>(a._1+b._1, a._2+b._2)).toList
  val p2 = ns.foldLeft((0,0,0))((a,b)=>b._1 match {
    case 'f'=>(a._1,       a._2+b._2, a._3+a._1*b._2)
    case 'u'=>(-b._2+a._1, a._2,      a._3)
    case 'd'=>(b._2+a._1,  a._2,      a._3) }).toList

  println(s"Part 1: ${ p1.product }, Part 2: ${ p2.tail.product }")