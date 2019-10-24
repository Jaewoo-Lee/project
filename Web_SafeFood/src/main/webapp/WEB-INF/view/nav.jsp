<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
	#back {
		text-align: center;
		width : 100%;
		height : 100px;
		background-color: rgb(192,192,192);	
	}
</style>
<title>Insert title here</title>
</head>
<body>

<%
	String id = (String)session.getAttribute("id");
	String name = (String)session.getAttribute("id");

%>

<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="list.do">Safe Fooood~</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="list.do">Home</a></li>
	   <li><a href="#">공지 사항</a></li>
	   <li><a href="list.do">상품 정보</a></li>
	   <li><a href="#">베스트 섭취 정보</a></li>
	   <li><a href="get.do">내 섭취 정보</a></li>
	   <li><a href="#">예상 섭취 정보</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
    
    <%
    	if(id == null) {
    %>

    <li><a href="signPage.mvc"><span class="glyphicon glyphicon-user"></span> Join </a></li>
    <%
    	}
    	else {
    		
    %>
    <li sytle="color:yellow;"><%=id%>님 </li>
   	<li><a href="infoPage.mvc"><span class="glyphicon glyphicon-user"></span> Info </a></li>
   	<li><a href="updatePage.mvc"><span class="glyphicon glyphicon-user"></span> Update </a></li>
   	<%
    	}
   	%>
      
    <%
    	if(id == null) {
    %>     
    	<li data-toggle="dropdown"><a href="#" ><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
    <%
    	}
    	else {
    %>
    	<li><a href="logout.do" ><span class="glyphicon glyphicon-log-in"></span> LogOut</a></li>
   <%
    	}
   	%>
	
	  <ul class="dropdown-menu">
		<li style="width:200px; height: 100px">
			<form method="post" action="loginSuccess.do">
				<div class="input-group">
					<span class="input-group-addon"><span class="input-group-text" id="inputGroup-sizing-sm">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Id&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
					</span> <input id="email"
						type="text" class="form-control" name="id"
						placeholder="id">
				</div>
				<div class="input-group">
					<span class="input-group-addon"><span class="input-group-text" id="inputGroup-sizing-sm">Password</span>
					</span> <input id="password"
						type="password" class="form-control" name="pass"
						placeholder="Password">
				</div>
				<button class="btn btn-primary" type="submit">login</button>
			</form>
		</li>
	  </ul>
		
      
    </ul>
  </div>
</nav>
<div id="back"></div>

</body>
</html>