package com.ssafy.model.repository;

import java.util.List;

import com.ssafy.model.dto.Food;

/** 인터페이스 */
public interface FoodRepository {
	public int insert(Food food);
	public List<Food> selectAll();
	public List<Food> searchByName(String name);
	public List<Food> searchByNutri(String name);
	public int choo(String name);
	public List<Food> searchCode(int code);
	public List<String> searchGotFood();
}
