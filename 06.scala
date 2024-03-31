#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit =
  val init = stdin.getLines().flatMap(_.split(',')).map(_.toInt)
            .foldLeft(Vector.fill(9)(0L))((a, i)=>a.updated(i, a(i)+1)).toList
  val tick = (x:List[Long]) => List(x(1),x(2),x(3),x(4),x(5),x(6),x(0)+x(7),x(8),x(0))
  val ticks = (n:Int) => (1 to n).foldLeft(init)((a,_)=>tick(a)).sum

  println(s"Part 1: ${ ticks(80) }, Part 2: ${ ticks(256) }")
