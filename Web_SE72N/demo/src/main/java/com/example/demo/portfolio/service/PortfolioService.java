package com.example.demo.portfolio.service;

import java.util.List;
import java.util.Map;

import com.example.demo.portfolio.dto.Portfolio;
import com.example.demo.portfolio.dto.PortfolioComment;
import com.example.demo.portfolio.dto.PortfolioDetail;

public interface PortfolioService {
	
	// 포트폴리오 리스트 조회 ( 포트폴리오, 포트폴리오 댓글 매핑해서 리턴)
	public List<PortfolioDetail> searchAllPortfolio();
	
	// 포트폴리오 글 작성 및 수정
	public List<PortfolioDetail> addPortfolio(Portfolio p);
	
	// 포트폴리오 댓글 작성 및 수정
	public List<PortfolioDetail> writePortfolioComment(PortfolioComment portfolioComment);
	
	// 포트폴리오 글 삭제
	public List<PortfolioDetail> deleteOne(int portNum);
	
	// 포트폴리오 댓글 삭제
	public List<PortfolioDetail> deletePortfolioComment(int portcommentNum);
}
