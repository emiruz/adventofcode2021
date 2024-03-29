#!/usr/bin/env scala

import scala.io.Source.stdin
import scala.util.chaining._

@main def aoc(): Unit = 
  val ns = stdin.getLines().map(_.toInt).toList
  val g = (a:Int, b:Int)  => if b > a then 1 else 0
  val f = (xs:List[Int]) => xs.pipe(ns=>ns.zip(ns.drop(1))).map(g.tupled).sum

  println(s"Part 1: ${ f(ns) }, Part 2: ${ f(ns.sliding(3).map(_.sum).toList) }")
