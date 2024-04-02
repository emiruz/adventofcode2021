#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit =
  val xs   = stdin.getLines().flatMap(_.split(',')).map(_.toInt).toVector
  val rng  = (xs.min to xs.max).toList
  val sums = (x:Int) => x * (x+1) / 2
  val p1   = rng.map(x=>(xs.map(y=>(y-x).abs).sum, x)).minBy(_._1)
  val p2   = rng.map(x=>(xs.map(y=>sums((y-x).abs)).sum, x)).minBy(_._1)
  
  println(s"Part 1: ${ p1._1 }, Part 2: ${ p2._1 }")
