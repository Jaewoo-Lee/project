package com.example.demo.token.service;

import java.util.List;

import com.example.demo.token.dto.Token;

public interface TokenService {
	// 토큰을 저장하는 작업
	public void receiveToken(Token token);
	
	// 토큰을 보내주는 작업
	public List<String> sendToken();
	
	// 차단한 토큰을 삭제
	public void deleteToken(Token token);
}
