<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
	import="java.util.*"    
    %>
    
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<style>
	#back {
		text-align: center;
		width : 100%;
		height : 100px;
		background-color: rgb(192,192,192);	
	}
	
	#center {
		display: inline-block;
	}
	
	.content{
		/* margin: 0px auto; */
		/* text-align: center; */
		margin: auto;
		width: 700px;
		text-align:center;
	}
	
	img {
		width:300px;
		height:300px;
	}
	
	#wrap{
		display: inline-block;
		text-align: center;
		width : 100%;
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


</style>


<!-- Load the AJAX API -->
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>



<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

<!--Script Start -->

<script type="text/javascript">

	$(document).ready(function(){
		//<![CDATA[

		// Load the Visualization API and the corechart package.
		// Visualization API및 corechart패키지를 로드합니다.
		google.charts.load('current', {
			'packages' : [ 'corechart' ]
		});

		// Set a callback to run when the Google Visualization API is loaded
		//Google Visualization API가 로드될 때 실행할 콜백을 설정합니다.
		google.charts.setOnLoadCallback(drawChart);

		//Callback that creates and populates a data table,
		//instantiates the pie chart, passes in the data and
		// draws it.
		//데이터 테이블을 만들고 채우는 콜백입니다.
		//원형 차트를 인스턴스화하고 데이터를 전달하며 그립니다.

		function drawChart() {
			
			let sup = Number($("#sup").text());
			let cal = Number($("#cal").text());
			let car = Number($("#car").text());
			let pro = Number($("#pro").text());
			let fat = Number($("#fat").text());
			let sug = Number($("#sug").text());
			let nat = Number($("#nat").text()) / 1000.0;
			let cho = Number($("#cho").text());
			let aci = Number($("#aci").text());
			let tra = Number($("#tra").text());
		
			
			//Create the data table.
			//데이터 테이블 생성
			var data = new google.visualization.arrayToDataTable([
				[ 'nutrition', 'g'],
				[ '탄수화물', car ],
				[ '단백질', pro ],
				[ '지방', fat ],
				[ '당류', sug ],
				[ '나트륨', nat ],
				[ '콜레스테롤', cho ],
				[ '포화지방산', aci ],
				[ '트랜스지방', tra ]
			]);

			// Set chart options
			// 차트 설정 옵션
			var options = {
				'title' : '영양 정보 (총용량: ' + sup + 'g), (칼로리: ' + cal + 'kcal)',
	 			'width' : 800,
				'height' : 500
			};

			//막대차트 변경시 범례가 잘리기 때문에 가로 세로 크기를 수정한다.
			//var options = {'title' : 'How Much Pizza I Ate Last Night', 'width' :500, 'height' : 400};

			//Instantiate and draw our chart, passing in some options.
			//옵션을 몇가지로 돌리면서 차트를 즉시 작성합니다.
			var chart = new google.visualization.PieChart(document
					.getElementById('chart_div'));
			//막대차트로 변경시 아래 주석을 풀면 된다.(변경된 점 PieChart -> BarChart)
			//var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
			chart.draw(data, options);
		}
		
	})
	
</script>

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


<h1> 상세 상품 정보</h1>
<div id="wrap">
	<div>
			<div class="content">
			<c:forEach var="item" items="${item}">
				<p style="display: none">${item.code}</p>
				<h4 style="text-align: center">${item.name}</h4>
				<p></p>

				<div style="width:400px; height:400px; display:inline-block"
				style="display:inline-block">
				<a href="specific.mvc?id=${item.code}"> 
				<img src="${item.img}" >
				</a>
				</div>
				<p>${item.maker}</p>

				<span>${item.material}</span> <span style="display: none"
					id="sup">${item.supportpereat}</span> <span
					style="display: none" id="cal">${item.calory}</span> <span
					style="display: none" id="car">${item.carbo}</span> <span
					style="display: none" id="pro">${item.protein}</span> <span
					style="display: none" id="fat">${item.fat}</span> <span
					style="display: none" id="sug">${item.sugar}</span> <span
					style="display: none" id="nat">${item.natrium}</span> <span
					style="display: none" id="cho">${item.chole}</span> <span
					style="display: none" id="aci">${item.fattyacid}</span> <span
					style="display: none" id="tra">${item.transfat}</span>
				</c:forEach>

				<!--Div that will hold the pie chart -->

				<!--파이 차트를 저장할 div-->

				<div id="chart_div"></div>
			</div>
		</div> <!-- content -->
	
</div> <!-- wrap -->



</body>

</body>
</html>