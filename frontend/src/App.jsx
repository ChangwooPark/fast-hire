function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white rounded-xl shadow-lg overflow-hidden md:max-w-2xl">
        <div className="md:flex">
          <div className="p-8">
            <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
              환경 구축 완료! 🚀
            </div>
            <h1 className="block mt-1 text-2xl leading-tight font-bold text-black">
              FastHire 프로젝트가 시작되었습니다
            </h1>
            <p className="mt-2 text-slate-500">
              현재 <span className="text-blue-600 font-mono font-bold">Tailwind CSS</span>가 성공적으로 적용되었습니다.
              이 화면이 깔끔하게 보인다면 모든 설정이 정상입니다.
            </p>
            
            <div className="mt-6 flex gap-4">
              <button className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition">
                구인 공고 올리기
              </button>
              <button className="px-4 py-2 border border-indigo-600 text-indigo-600 rounded-lg hover:bg-indigo-50 transition">
                DM 보내기
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App