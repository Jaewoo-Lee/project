package com.example.demo.token.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.token.dto.Token;

public interface TokenRepository  extends JpaRepository<Token, String>{

}
