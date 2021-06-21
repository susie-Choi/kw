import java.util.Scanner;

public class Main {

	private static Scanner sc;
	private static MenuSelect ms;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("광운대학교 정보융합학부 2017204081 최수지의 프로젝트입니다.");

		boolean run = true;
		sc = new Scanner(System.in);
		ms = MenuSelect.getInstance();

		while (run) {
			showMainMenu();
			try {
				int select = sc.nextInt();
			} catch (Exception e) {
				System.out.println("다시 입력해주세요!"); // 숫자 입력이 아닌 경우 예외처리
			} finally {
				System.out.print("1|2|3|4 중 입력 해주세요 : "); // 예외 처리로 인해 한번 더 입력하기
				int select = sc.nextInt();
				switch (select) {
				case Menu.QUIT:
					run = false;
					System.out.println("프로그램을 종료합니다.");
					break;

				case Menu.INSERT:
					insertContact();
					break;

				case Menu.SELECT_ALL:
					selectAllContact();
					break;

				case Menu.DELETE:
					deleteIndexContact();
					break;

				default:
					System.out.println("선택지가 없습니다. 다시 골라주세요.");
				}
			}
		}
		sc.close();
	}

	static void showMainMenu() { // 메뉴
		System.out.println();
		System.out.println("내 주소록 ");
		System.out.println("[1:등록 | 2:삭제 | 3:전체검색 | 4:종료]");
		System.out.print("원하는 번호를 골라주세요 : ");
	}

	static void insertContact() { // 등록
		System.out.println();
		System.out.println("[등록]");

		System.out.print("이름을 입력 해주세요 : ");
		String name = sc.next();

		System.out.print("연락처를 입력 해주세요 : ");
		String phone = sc.next();

		People contact = new People(name, phone);

		int result = ms.insert(contact);

		if (result > 0) {
			System.out.println("등록 성공");
		} else {
			System.out.println("등록 실패");
		}
	}

	static void selectAllContact() { // 전체 연락처
		if (ms.select().isEmpty()) {
			System.out.println("현재 연락처 내부에 데이터가 없습니다.");
		} else {
			System.out.println("전체 연락처 목록");
			for (People num : ms.select()) {
				System.out.print(ms.select().indexOf(num) + " ");
				System.out.println(num);
			}
		}
	}

	static void deleteIndexContact() { // 연락처 지우기
		if (ms.select().isEmpty()) {
			System.out.println("현재 연락처 내부에 데이터가 없습니다.");
		} else {
			System.out.println();
			System.out.print("삭제할 사람의 번호를 입력해주세요 : ");
			int index = sc.nextInt();
			sc.next();

			if (index < ms.select().size()) {
				if (index > 0) {
					int result = ms.delete(index);
					System.out.println("삭제되었습니다.");
				} else
					System.out.println("다시 시도해주세요.");
			} else {
				System.out.println("다시 시도해주세요");
			}
		}
	}
}