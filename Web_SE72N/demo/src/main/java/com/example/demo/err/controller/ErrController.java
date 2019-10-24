package com.example.demo.err.controller;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import lombok.extern.slf4j.Slf4j;

@Controller
@Slf4j
public class ErrController implements ErrorController {
	
	@GetMapping("/error")
	public String redirectRoot() {
		//log.debug("에러페이지!!");
		return "../static/index";
	}
	
	@Override
	public String getErrorPath() {
		return "/error";
	}
}
