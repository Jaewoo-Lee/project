package com.ssafy.model.service;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dto.Food;
import com.ssafy.model.repository.FoodRepository;

@Service
public class FoodServiceImpl implements FoodService {
	@Autowired
	private FoodRepository foodRepo;
	
	// 로그 찍을 객체
	static final Logger logger = LoggerFactory.getLogger(FoodServiceImpl.class); // import org.slf4j.Logger;
	
	public List<Food> getFoodList() {
		logger.debug("getFoodList 호출"); // logger 에는 레벨과 출력 방법을 지정 할수있다.
		return foodRepo.selectAll();
	}
	public List<String> searchGotFood() {
		logger.debug("searchGotFood 호출"); // logger 에는 레벨과 출력 방법을 지정 할수있다.
		return foodRepo.searchGotFood();
	}
	public List<Food> searchByName(String name) {
		logger.debug("searchName 호출"); // logger 에는 레벨과 출력 방법을 지정 할수있다.
		return foodRepo.searchByName(name);
	}
	public List<Food> searchByNutri(String name) {
		logger.debug("searchNutri 호출"); // logger 에는 레벨과 출력 방법을 지정 할수있다.
		return foodRepo.searchByNutri(name);
	}
	public int addFood(Food food) {
		logger.debug("addFood 호출");
		return foodRepo.insert(food);
	}
	public int FoodChoo(String name) {
		logger.debug("FoodChoo 호출");
		
		//중복 검사하기
		List<Food> tlist = foodRepo.searchByName(name);
		if(tlist.size() > 0) return 0;
		else return foodRepo.choo(name);
	}
	public List<Food> searchByCode(int code) {
		logger.debug("searchByCode 호출");
		return foodRepo.searchCode(code);
	}
}
// 작성 완료후 구현한 레파지토리 객체와 서비스객체를 컨테이너에 빈으로 등록하기 (컨트롤러에 작업)

