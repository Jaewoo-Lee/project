package com.ssafy.model.repository;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.ssafy.model.dto.Food;

// 인터페이스를 구현한 클래스
@Repository
public class FoodRepositoryImpl implements FoodRepository {
	@Autowired
	private SqlSession session;
	
	private static final String namespace = "mybatis.foodMapper."; // .까지 문자열로 준비
	
	// selectAll 을 부르려면 풀네임 mybatis.foodMapper.selectAll 로 표현할 수 있다	
	public List<Food> selectAll() {
		return session.selectList(namespace+"selectAll");
	}
	public List<Food> searchByName(String name) {
		return session.selectList(namespace+"searchByName", "%"+name+"%");
	}
	public List<Food> searchByNutri(String name) {
		return session.selectList(namespace+"searchByNutri", "%"+name+"%");
	}
	
	public int insert(Food food) {
		return session.insert(namespace + "insert", food);
	}
	public int choo(String name) {
		return session.insert(namespace + "foodChoo", name);
	}
	public List<Food> searchCode(int code) {
		return session.selectList(namespace + "searchByCode", code);
	}
	public List<String> searchGotFood() {
		return session.selectList(namespace+"searchGot");
	}
}
// SqlSessionTemplate 를 주입받아서, 각함수에 적절한 쿼리문을 호출하도록 구현