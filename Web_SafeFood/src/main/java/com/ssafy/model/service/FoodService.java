package com.ssafy.model.service;

import java.util.List;

import com.ssafy.model.dto.Food;


public interface FoodService {
	public List<Food> getFoodList();
	public List<Food> searchByName(String name);
	public List<Food> searchByNutri(String name);
	public int addFood(Food food);
	public int FoodChoo(String name);
	public List<Food> searchByCode(int code);
	public List<String> searchGotFood();
}
