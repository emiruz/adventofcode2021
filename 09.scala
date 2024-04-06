#!/usr/bin/env scala
import scala.io.Source.stdin

@main def aoc(): Unit =
  val ps    = List((0,-1),(0,1),(-1,0),(1,0))
  val rs    = stdin.getLines().map { _.map(_.asDigit).toList }.toList
  val (n,m) = (rs.length, rs(0).length)
  val adj   = (i:Int, j:Int) => for { (a,b) <- ps if n>a+i && a+i>=0 && m>b+j && b+j>=0 } yield (a+i,b+j)
  val comp  = (i:Int, j:Int) => adj(i,j).forall(rs(i)(j) < rs(_)(_))
  val lps   = for { i<-(0 to n-1); j<-(0 to m-1) if comp(i,j) } yield (i,j)
  val B_    = (i:Int, j:Int) => adj(i,j).filter { (a,b) => rs(i)(j) < rs(a)(b) && rs(a)(b) < 9 }

  def Br(i:Int, j:Int): List[(Int,Int)] = B_(i,j).flatMap( Br.tupled ) ++ B_(i,j)

  val B     = (i:Int, j:Int) => Br(i,j).appended((i,j)).distinct
  val p2    = lps.map { (i,j)=> B(i,j).length }.sorted

  println(s"Part 1: ${ lps.map(1+rs(_)(_)).sum }, Part 2: ${ p2.takeRight(3).product }")
