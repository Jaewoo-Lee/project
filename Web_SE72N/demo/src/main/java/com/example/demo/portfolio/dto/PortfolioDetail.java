package com.example.demo.portfolio.dto;

import java.time.LocalDateTime;
import java.util.List;

import lombok.Data;

@Data
public class PortfolioDetail {
	private Integer portNum;
	private String portTitle;
	private String portContent;
	private LocalDateTime portDatetime;
	private String portImg;
	private String userId;
	private List<PortfolioComment> commentList;
	
	public PortfolioDetail(Portfolio p){
		this.portNum = p.getPortNum();
		this.portTitle = p.getPortTitle();
		this.portContent = p.getPortContent();
		this.portDatetime = p.getPortDatetime();
		this.portImg = p.getPortImg();
		this.userId = p.getUserId();
	}
}
