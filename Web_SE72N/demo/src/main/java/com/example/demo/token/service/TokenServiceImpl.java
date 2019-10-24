package com.example.demo.token.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.token.dto.Token;
import com.example.demo.token.repository.TokenRepository;

@Service
public class TokenServiceImpl implements TokenService {
	@Autowired
	private TokenRepository tokenRepository;
	
	// 토큰을 저장하는 작업
	@Override
	public void receiveToken(Token token) {
		tokenRepository.save(token);
	}

	// 토큰을 보내주는 작업
	@Override
	public List<String> sendToken() {
		List<Token> temp = tokenRepository.findAll();
		List<String> list = new ArrayList<>();
		for (Token token : temp) {
			list.add(token.getTokenInfo());
		}
		return list;
	}

	// 토큰을 삭제하는 작업
	@Override
	public void deleteToken(Token token) {
		tokenRepository.delete(token);
	}

}
