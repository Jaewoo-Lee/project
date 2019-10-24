package com.example.demo.user.service;

import java.util.List;
import java.util.Map;

import com.example.demo.user.dto.Authorities;
import com.example.demo.user.dto.User;
import com.example.demo.user.dto.UserInfo;

public interface UserService {
	// 로그인 확인
	public UserInfo login(User user);
	
	// 회원가입
	public boolean addUser(User user);
	
	// 유저의 권한 리스트 조회
	public List<Authorities> searchAuthorities();

	// 유저의 권한 변경 ( 관리자만 )
	public List<Authorities> changeAuthority(Authorities authority);
}
