package com.example.demo.portfolio.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import com.example.demo.portfolio.dto.PortfolioComment;

public interface PortfolioCommentRepository extends JpaRepository<PortfolioComment, Integer> {

	@Modifying
	@Transactional
	@Query(value = "DELETE FROM PortfolioComment WHERE portNum = ?1")
	void deleteByPortNum(int portNum);
	
}
