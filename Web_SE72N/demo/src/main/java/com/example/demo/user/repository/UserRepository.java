package com.example.demo.user.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.example.demo.user.dto.User;
import com.example.demo.user.dto.UserInfo;

public interface UserRepository extends JpaRepository<User, String>{
	
}
