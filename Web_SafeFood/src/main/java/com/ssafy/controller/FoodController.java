package com.ssafy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.ssafy.model.dto.Food;
import com.ssafy.model.service.FoodService;

@Controller // 앞에 @Controller 붙인 클래스는 디스페처가 받은 요청을 처리할 페이지를 결정해주는 클래스
public class FoodController {
	@Autowired
	private FoodService fService;
	// 서버가 구현해야될 요청
	// list.do 상품 전체목록을 보여달라는 요청
	// addForm.do 상품을 등록할 페이지 요청
	// add.do 상품을 추가해달라는 요청

	@RequestMapping("list.do") // 매핑하는 방법도 여러가지가 있지만 쉬운방법 1가지로 통일함
	public String list(Model model) {
		model.addAttribute("list", fService.getFoodList());
		return "front";
	}

	@RequestMapping("addForm.do")
	public String addForm() {
		return "addForm";
	}

	@RequestMapping("add.do")
	public String add(Food food) { // 필요한 파라미터가 있는 경우 나열만하면, 알아서 값을 넣어줌
		fService.addFood(food); // 정보를 입력후에 입력결과를 보기위해 목록을 보여주면 좋겠다 그래서 아래
		return "redirect:list.do"; // 리다이렉트 list.do 로
	}

	@RequestMapping("search.do")
	public String search(Model model, String category, String data) {
		if (category.equals("name")) {
			model.addAttribute("list", fService.searchByName(data));
		} else
			model.addAttribute("list", fService.searchByNutri(data));
		return "front";
	}

	@RequestMapping("searchByName.do")
	public String searchByName(Model model, String name) {
		model.addAttribute("item", fService.searchByCode(fService.searchByName(name).get(0).getCode()));
		return "specific";
	}

	@RequestMapping("FoodChoo.do")
	public String foodChoo(String name) {
		fService.FoodChoo(name);
		return "redirect:list.do";
	}

	@RequestMapping("specific.do")
	public String specific(Model model, int code) {
		model.addAttribute("item", fService.searchByCode(code));
		return "specific";
	}

	@RequestMapping("get.do")
	public String getFood(Model model) {
		model.addAttribute("list", fService.searchGotFood());
		return "gotFood";
	}

//	//user
//	@RequestMapping("loginSuccess.do")
//	public String login(Model model) { // 필요한 파라미터가 있는 경우 나열만하면, 알아서 값을 넣어줌 
//		model.addAttribute("id", fSer); // 정보를 입력후에 입력결과를 보기위해 목록을 보여주면 좋겠다 그래서 아래
//		return "redirect:front.do"; // 리다이렉트 list.do 로
//	}
//	@RequestMapping("logout.do")
//	public String logout(Model model) { // 필요한 파라미터가 있는 경우 나열만하면, 알아서 값을 넣어줌 
//		model.addAttribute("id", null); // 정보를 입력후에 입력결과를 보기위해 목록을 보여주면 좋겠다 그래서 아래
//		return "redirect:front.do"; // 리다이렉트 list.do 로
//	}
}
