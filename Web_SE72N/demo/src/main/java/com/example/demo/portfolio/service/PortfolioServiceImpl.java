package com.example.demo.portfolio.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import com.example.demo.portfolio.dto.Portfolio;
import com.example.demo.portfolio.dto.PortfolioComment;
import com.example.demo.portfolio.dto.PortfolioDetail;
import com.example.demo.portfolio.repository.PortfolioCommentRepository;
import com.example.demo.portfolio.repository.PortfolioRepository;

@Service
public class PortfolioServiceImpl implements PortfolioService {
	@Autowired
	private PortfolioRepository portfolioRepository;
	@Autowired
	private PortfolioCommentRepository portfolioCommentRepository;
	
	// 포트폴리오 리스트 조회 ( 포트폴리오, 포트폴리오 댓글 매핑해서 리턴)
	@Override
	public List<PortfolioDetail> searchAllPortfolio() {
		List<Portfolio> plist = portfolioRepository.findAll(new Sort(Sort.Direction.DESC, "portNum"));
		List<PortfolioComment> pclist = portfolioCommentRepository.findAll(new Sort(Sort.Direction.ASC, "portcommentNum"));
		List<PortfolioDetail> pdlist = new ArrayList<>();
		for (Portfolio p : plist) {
			PortfolioDetail temp = new PortfolioDetail(p);
			List<PortfolioComment> tempList = new ArrayList<>();
			for (PortfolioComment pc : pclist) {
				if(temp.getPortNum().equals(pc.getPortNum())) {
					tempList.add(pc);
				}
			}
			temp.setCommentList(tempList);
			pdlist.add(temp);
		}
		return pdlist;
	}

	// 포트폴리오 글 작성 및 수정
	@Override
	public List<PortfolioDetail> addPortfolio(Portfolio portfolio) {
		if(portfolio.getPortNum() == -1) portfolio.setPortNum(null);
		portfolioRepository.save(portfolio);
		return searchAllPortfolio();
	}

	// 포트폴리오 댓글 작성 및 수정
	@Override
	public List<PortfolioDetail> writePortfolioComment(PortfolioComment portfolioComment) {
		if(portfolioComment.getPortcommentNum() == -1) portfolioComment.setPortcommentNum(null);
		portfolioCommentRepository.save(portfolioComment);
		return searchAllPortfolio();
	}

	// 포트폴리오 글 삭제
	@Override
	public List<PortfolioDetail> deleteOne(int portNum) {
		portfolioRepository.deleteById(portNum);
		portfolioCommentRepository.deleteByPortNum(portNum);
		return searchAllPortfolio();
	}

	// 포트폴리오 댓글 삭제
	@Override
	public List<PortfolioDetail> deletePortfolioComment(int portcommentNum) {
		portfolioCommentRepository.deleteById(portcommentNum);
		return searchAllPortfolio();
	}
}
