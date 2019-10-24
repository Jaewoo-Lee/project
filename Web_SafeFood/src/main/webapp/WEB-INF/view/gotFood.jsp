<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<div style="text-align: center;">
	<h1>내가 먹은 음식의 목록</h1>
	<c:forEach var="list" items="${list}">
		<a href="searchByName.do?name=${list }">
		<h3>${list.toString() }</h3>
		</a>
	</c:forEach>
	</div>
</body>
</html>