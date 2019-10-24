package com.example.demo.portfolio.controller;

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
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.portfolio.dto.Portfolio;
import com.example.demo.portfolio.dto.PortfolioComment;
import com.example.demo.portfolio.dto.PortfolioDetail;
import com.example.demo.portfolio.service.PortfolioService;

import lombok.extern.slf4j.Slf4j;

@CrossOrigin
@Controller
@Slf4j
public class PortfolioController {
	@Autowired
	private PortfolioService portfolioService;
	
	// 포트폴리오 리스트 조회
	@GetMapping("/searchAllPortfolio.do")
	public ResponseEntity<List<PortfolioDetail>> searchAllPortfolio() {
		log.debug("portfolio 리스트 호출");
		return new ResponseEntity<List<PortfolioDetail>>(portfolioService.searchAllPortfolio(), HttpStatus.OK);
	}
	
	// 포트폴리오 글 작성 및 수정
	@PostMapping("/newPortfolio.do")
	public ResponseEntity<List<PortfolioDetail>> addPortfolio(@RequestBody Portfolio portfolio){
		log.debug("portfolio 저장 요청");
		return new ResponseEntity<List<PortfolioDetail>>(portfolioService.addPortfolio(portfolio), HttpStatus.OK);
	}
	
	// 포트폴리오 댓글 작성 및 수정
	@PostMapping("/writePortfolioComment.do")
    public ResponseEntity<List<PortfolioDetail>> writeComment(@RequestBody PortfolioComment portfolioComment){
    	log.debug("portfolioComment 저장 요청");
    	return new ResponseEntity<List<PortfolioDetail>>(portfolioService.writePortfolioComment(portfolioComment), HttpStatus.OK);
    }
	
	// 포트폴리오 글 삭제
	@DeleteMapping("/deletePortfolio.do")
    public ResponseEntity<List<PortfolioDetail>> deletePortfolio(@RequestParam int portNum){
    	log.debug(portNum + "번 portfolio 게시글 삭제 요청");
    	return new ResponseEntity<List<PortfolioDetail>>(portfolioService.deleteOne(portNum), HttpStatus.OK);
    }
	
	// 포트폴리오 댓글 삭제
	@DeleteMapping("/deletePortfolioComment.do")
    public ResponseEntity<List<PortfolioDetail>> deletePortfolioComment(@RequestParam int portcommentNum){
    	log.debug(portcommentNum + "번 portfolioComment 댓글 삭제 요청");
    	return new ResponseEntity<List<PortfolioDetail>>(portfolioService.deletePortfolioComment(portcommentNum), HttpStatus.OK);
    }
}
