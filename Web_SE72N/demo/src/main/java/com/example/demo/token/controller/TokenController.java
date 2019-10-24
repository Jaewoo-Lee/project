package com.example.demo.token.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.example.demo.token.dto.Token;
import com.example.demo.token.service.TokenService;

import lombok.extern.slf4j.Slf4j;

@CrossOrigin
@Controller
@Slf4j
public class TokenController {
	@Autowired
	private TokenService tokenService;
	
	// 토큰을 저장하는 작업
	@PostMapping("/saveToken.do")
	public ResponseEntity<String> receiveToken(@RequestBody Token token){
		log.debug("token 저장");
		tokenService.receiveToken(token);
		return new ResponseEntity<String>("", HttpStatus.OK);
	}
	
	// 토큰을 보내주는 작업
	@GetMapping("/findToken.do")
	public ResponseEntity<List<String>> sendToken(){
		log.debug("token list 조회");
		return new ResponseEntity<List<String>>(tokenService.sendToken(), HttpStatus.OK);
	}
	
	// 토큰을 삭제하는 작업
	@DeleteMapping("/deleteToken.do")
	public ResponseEntity<String> deleteToken(@RequestBody Token token){
		log.debug("token 삭제 요청");
		tokenService.deleteToken(token);
		return new ResponseEntity<String>("성공", HttpStatus.OK);
	}
}
