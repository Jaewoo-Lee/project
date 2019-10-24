package com.example.demo.user.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.example.demo.user.dto.Authorities;
import com.example.demo.user.dto.User;
import com.example.demo.user.dto.UserInfo;
import com.example.demo.user.service.UserService;

import lombok.extern.slf4j.Slf4j;

@CrossOrigin
@Controller
@Slf4j
public class UserController {
	@Autowired
	private UserService userService;
	
	// 로그인 확인
	@PostMapping("/login.do")
	public ResponseEntity<UserInfo> login(@RequestBody User user) {
		log.debug("login 요청");
		return new ResponseEntity<UserInfo>(userService.login(user), HttpStatus.OK);
	}

	// 회원가입
	@PostMapping("/addUser.do")
	public ResponseEntity<Boolean> addUser(@RequestBody User user){
		log.debug("회원가입 요청");
		return new ResponseEntity<Boolean>(userService.addUser(user), HttpStatus.OK);
	}
	
	// 유저의 권한 리스트 조회
	@GetMapping("/searchAuthorities.do")
	public ResponseEntity<List<Authorities>> searchAuthorities() {
		log.debug("유저 권한 조회");
		return new ResponseEntity<List<Authorities>>(userService.searchAuthorities(), HttpStatus.OK);
	}
	
	// 유저의 권한 변경 ( 관리자만 )
	@PostMapping("/changeAuthority.do")
	public ResponseEntity<List<Authorities>> changeAuthority(@RequestBody Authorities authority) {
		log.debug(authority.getUserId() + " 의 권한을 " + authority.getAuthority() + "로 변경");
		return new ResponseEntity<List<Authorities>>(userService.changeAuthority(authority), HttpStatus.OK);
	}
}
