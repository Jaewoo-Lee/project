<!DOCTYPE html>
<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" 
	pageEncoding="UTF-8" import="java.util.*"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<style>
#back {
	text-align: center;
	width: 100%;
	height: 100px;
	background-color: rgb(192, 192, 192);
}

#center {
	display: inline-block;
}

#content {
	/* margin: 0px auto; */
	/* text-align: center; */
	display: inline-block;
}

img {
	width: 300px;
	height: 300px;
}

#wrap {
	text-align: center;
	width: 100%;
}

.cont {
	text-align: center;
	width: 900px;
}

.inline {
	display: inline-block;
	height: 100%;
}

h1 {
	text-align: center;
}

.item {
	margin-bottom: 30px;
}

.pdlist.col-md-3.item{
	border: 1px solid #aaa;
	margin-left: 15px;
	margin-right: 15px;
	width : 350px;
}

.gotit{
	margin-top:10px;
}
</style>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

<!-- jQuery library -->
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script
	src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>


</head>
<body>
	<jsp:include page="./nav.jsp" />

	<div id="back">
		<div id="center">
			<div class="input-group">
				<form method="get" action="search.do">
					<select name="category" style="width:80px;height:20px;">
						<option value="name">제품명</option>
						<option value="nutri">영양</option>
					</select>
					<input id="search" name="data" type="text" class="form-control"
						placeholder="Search">
					<div class="input-group-btn">
						<button type="submit" id="btn_search" class="btn btn-default">
							<i class="glyphicon glyphicon-search"></i>
						</button>
					</div>
				</form>

			</div>

		</div>
	</div>


	<h1>전체 상품</h1>
	<div id="wrap">
		<div id="content">
			<c:forEach var="list" items="${list}">
				<div class="pdlist col-md-3 item"><br>
					<a href="specific.do?code=${list.code}"> 
						<img src="${list.img}"/>
					</a>
					<a href="FoodChoo.do?name=${list.name}"><button class="gotit">먹었다!</button></a>
					<h3 style="text-align: center">${list.name}</h3>
					<p></p>


				</div>
				
			</c:forEach>
		</div>
		<!-- content -->

	</div>
	<!-- wrap -->
</body>
</html>
