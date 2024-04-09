#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit =
  val pos = "([{<"
  val neg = ")]}>"
  val ps1 = Map(')'->3, ']'->57, '}'->1197, '>'->25137)
  val ps2 = Map(')'->1, ']'->2, '}'->3, '>'->4)
  val ls  = stdin.getLines().toList

  def parse(xs:List[Char], es:List[Char]=List.empty): (Option[Char], List[Char]) = 
    val i = if xs.nonEmpty then pos.indexOf(xs(0)) else -1
    val n = if i == -1 then List() else List(neg(i))
    xs match
      case x :: t if es.isEmpty => parse(t, n)
      case x :: t if pos.contains(x) => parse(t, n ++ es)
      case x :: t if es.nonEmpty && x != es(0) => (Some(x), es)
      case x :: t => parse(t, es.tail)
      case _ => (None, es)

  val p1    = ls.flatMap{ x=>parse(x.toList)._1 }.collect(ps1(_)).sum
  val score = (xs:List[Char]) => xs.map(ps2(_).toLong).foldLeft(0L){ (a,x)=> a*5+x }
  val p2    = ls.map{ x=>parse(x.toList) }.collect { case (None, x) => score(x) }.sorted

  println(s"Part 1: ${ p1 }, Part 2: ${ p2(p2.length / 2)  }")
