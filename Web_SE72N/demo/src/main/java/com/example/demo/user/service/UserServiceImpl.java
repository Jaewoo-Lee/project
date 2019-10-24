package com.example.demo.user.service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.portfolio.repository.PortfolioRepository;
import com.example.demo.post.repository.PostRepository;
import com.example.demo.user.dto.Authorities;
import com.example.demo.user.dto.User;
import com.example.demo.user.dto.UserInfo;
import com.example.demo.user.repository.AuthoritiesRepository;
import com.example.demo.user.repository.UserRepository;
import com.example.demo.util.SecurityUtil;

@Service
public class UserServiceImpl implements UserService {
	@Autowired
	private UserRepository userRepository;
	@Autowired
	private AuthoritiesRepository authoritiesRepository;
	// 로그인 확인
	@Override
	public UserInfo login(User user) {
		Optional<User> maybeUser = userRepository.findById(user.getUserId());
		UserInfo maybeInfo = new UserInfo();
		if(maybeUser.isPresent() &&	// maybeUSer에 값이 있으면서 (DB에 id와 일치하는 게 있음)
				new SecurityUtil().encodeSHA256(user.getUserPass()).equals(maybeUser.get().getUserPass())) {	// password가 일치하면
			// Authorities에서 권한을 찾아오기
			maybeInfo.setAuthority(authoritiesRepository.findById(user.getUserId()).get().getAuthority());
			maybeInfo.setGithubId(maybeUser.get().getGithubId());
			maybeInfo.setUserId(maybeUser.get().getUserId());
		} else {
			maybeInfo.setAuthority("GUEST");
		}
		return maybeInfo;
	}
	
	// 회원가입
	@Override
	public boolean addUser(User user) {
		Optional<User> maybeUser = userRepository.findById(user.getUserId());
		if(maybeUser.isPresent()) {	// maybeUser에 값이 있으면 회원가입을 못하게 한다.
			return false;
		} else {
			user.setUserPass(new SecurityUtil().encodeSHA256(user.getUserPass()));	// 패스워드를 암호화 해서 저장
			userRepository.save(user);
			Authorities auth = new Authorities();
			auth.setUserId(user.getUserId());
			auth.setAuthority("VISITOR");
			authoritiesRepository.save(auth);
			return true;
		}
	}

	// 유저의 권한 리스트 조회
	@Override
	public List<Authorities> searchAuthorities() {
		return authoritiesRepository.findAll();
	}
	
	// 유저의 권한 변경 ( 관리자만 )
	@Override
	public List<Authorities> changeAuthority(Authorities authority) {
		authoritiesRepository.save(authority);
		return searchAuthorities();
	}
}
